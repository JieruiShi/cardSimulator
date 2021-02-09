from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

myList = []

class hello(Resource):
    def get(self):
        return myList

api.add_resource(hello, '/hello')

class hello2(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('add', type = str, required = True, location = 'json')

    def post(self):
        args = self.reqparse.parse_args()
        added = args['add']
        myList.append(added)
        return

api.add_resource(hello2, '/hello2')

if __name__ == '__main__':
    app.run(debug = True)
