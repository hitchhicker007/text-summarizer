from script import generate_summary
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Generate(Resource):

    def post(self):
        json_data = request.get_json(force=True)
        text = json_data['text']

        summary = generate_summary(text, 3)

        return jsonify(summary=summary)

api.add_resource(Generate,'/generate')

if __name__ == '__main__':
    app.run()