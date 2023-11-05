from flask import Flask, jsonify
from flask_cors import CORS
from piazza_api import Piazza
import piazza_fun



# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/", methods=['GET'])
def index():
    return "Hello Piazza"

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

@app.route("/<int:class_id>/<str:folder_name>", methods=['GET'])
def get_folder_posts(class_id, folder_name):
    p = Piazza()
    p.user_login("Eryka.shishun@mail.utoronto.ca", "newhacks2023")


    course  = p.network(class_id)
    filters = course.feed_filters
    filtered_posts = course.get_filtered_feed(filters[2](folder_name))

    feed_posts = filtered_posts["feed"]
    
    good_feed_posts_list = piazza_fun.find_credible_filtered_posts(feed_posts)
    post_details = piazza_fun.get_post_details_list(course, good_feed_posts_list)


    return post_details


if __name__ == "__main__":
    app.run(debug=True, port=8080)