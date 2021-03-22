from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class GetData(Resource):
    def get(self):
        print("Hello Bit World - on API server")
        return { "Value" : "Hello Bit World - to client" }

api.add_resource(GetData, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5001)