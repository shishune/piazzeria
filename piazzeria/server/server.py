from flask import Flask, jsonify
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

# /api/home
@app.route("/members", methods=['GET'])
def members():
    return jsonify({
        'members': ['Jack', 'Harry', 'Arpan']
    })


if __name__ == "__main__":
    app.run(debug=True, port=8080)