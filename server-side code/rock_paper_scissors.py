from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

game = {
    'register': {
        'player1': None, #token for player1, None for empty
        'player2': None, #token for player2, None for empty
    },
    'status': {
        'player1': None, #0/1/2, None for not received yet
        'player2': None, #0/1/2, None for not received yet
        'previousGame': None, #1 for player1's win, 2 for player2's win， 0 for tie
    },
    'wins': {
        'player1': 0,
        'player2': 0,
        'tie': 0
    }
}

# class hello2(Resource):
#
#     def __init__(self):
#         self.reqparse = reqparse.RequestParser()
#         self.reqparse.add_argument('add', type = str, required = True, location = 'json')
#
#     def post(self):
#         args = self.reqparse.parse_args()
#         added = args['add']
#         myList.append(added)
#         return
#
# api.add_resource(hello2, '/hello2')

class register(Resource):
    def get(self):
        for


        return game['register']['player1']

api.add_resource(register, '/register')

if __name__ == '__main__':
    app.run(debug = True)
