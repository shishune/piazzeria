from flask import Flask, jsonify
from flask_cors import CORS
from piazza_api import Piazza
import piazza_fun
import cohere


# app instance
app = Flask(__name__)
CORS(app)

# /api/home
# @app.route("/", methods=['GET'])
# def index():
#     return "Hello Piazza"

@app.route("/credits", methods=['GET'])
def index():
    return "By Derek Eryka Grace Kevin"

# class ClassnNetwork(Resource):
#     def login(email, password):

@app.route("/classes", methods=['GET'])
def get_classes():
    p = Piazza()
    p.user_login("Eryka.shishun@mail.utoronto.ca", "newhacks2023")

    return p.get_user_classes()

@app.route("/<int:class_id>", methods=['GET'])
def get_foldera(class_id):
    return piazza_fun.get_all_folders(class_id)

@app.route("/<int:class_id>/<string:folder_name>", methods=['GET'])
def get_folder_posts(class_id, folder_name):
    p = Piazza()
    p.user_login("Eryka.shishun@mail.utoronto.ca", "newhacks2023")


    course  = p.network(class_id)
    filters = course.feed_filters
    filtered_posts = course.get_filtered_feed(filters[2](folder_name))

    feed_posts = filtered_posts["feed"]
    
    good_feed_posts_list = piazza_fun.find_credible_filtered_posts(feed_posts)
    post_details = piazza_fun.get_post_details_list(course, good_feed_posts_list)
    sorted_post_details = sorted(post_details, key=lambda x: x['endorsers_num'], reverse=True)

    #derek's code below
    api_key = "PeCmHb0BGFJIEfHlNsxRLDPyvXTxsa168UAR0WSD"

    co = cohere.Client(api_key)
    
    response = co.generate(
      model='command',
      prompt="clean the text so each question has an answer:" + str(sorted_post_details[1:]),
      temperature=0.9,
      k=0,
      stop_sequences=[],
      return_likelihoods='NONE')
    #print('Prediction: {}'.format(response.generations[0].text))
    output_data = 'Prediction: {}'.format(response.generations[0].text)

    return output_data


if __name__ == "__main__":
    app.run(debug=True, port=8080)
