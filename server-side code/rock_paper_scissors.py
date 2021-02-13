from flask import Flask
from flask_restful import Api, Resource, reqparse
import secrets
import utils

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
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('token', type = str, required = True, location = 'json')

    def get(self):
        register = game['register']
        for player in register:
            if register[player] == None:
                token = secrets.token_hex(4)
                register[player] = token
                print(game)
                return token
        else:
            return -1

    def post(self):
        args = self.reqparse.parse_args()
        token = args['token']

        for player in register:
            if register[player] == token:
                register[player] = None
                print(game)
                return 1
        else:
            return -1



class status(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('token', type = str, required = True, location = 'json')
        self.reqparse.add_argument('move', type = int, required = True, location = 'json')

    def post(self):
        args = self.reqparse.parse_args()
        token = args['token']
        move = args['move']
        register = game['register']
        player = utils.get_key(register, token)
        if player != -1:
            game[player] = move
            return 1
        else:
            return -1

class wins(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('token', type = str, required = True, location = 'json')


    def get(self):
        args = self.reqparse.parse_args()
        token = args['token']
        register = game['register']
        for player in register:
            if register[player] == token:
                player_number = utils.get_key(register,token)
                win_number = game['wins'][player_number]
                return win_number

        else:
            return -1




api.add_resource(register, '/register')

if __name__ == '__main__':
    app.run(debug = True)
