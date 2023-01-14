from flask import Flask, jsonify
from flask_restful import Api, reqparse

app = Flask(__name__)
api = Api(app)

questions = [
    {
        "Q": "What" and "gyan",
        "A": "Gyan mela is test test test"
    },
    {
        "Q":"what" and "program",
        "A": "This is a program made by meeeeeeeee"
    }
]

@app.route('/get-request')
def get_request():
    return jsonify(questions), 200

@app.route('/post-request')
def post_request():
    parser = reqparse.RequestParser()
    parser.add_argument("question")
    params = parser.parse_args()

    for question in questions:
        if question["Q"] in params["question"]:
            return question["A"], 200
    return "Sorry, not found", 404

if __name__ == '__main__':
    app.run(debug=True)
