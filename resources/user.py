import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help='This field is required.'
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help='This field is required.'
    )

    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):     #check to see if user exists.
            return{'message':'{} is already registered.'.format(data['username'])}, 400

        user = UserModel(data['username'],data['password'])
        user.save_to_db()
        
        return{'message':'User created successfully.'}, 201
