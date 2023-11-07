from flask import Flask, request
from flask_restful import Api, Resource, reqparse
import sqlite3

app = Flask(__name__)
api = Api(app)

# Define a parser to parse request data
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username is required')
parser.add_argument('password', type=str, required=True, help='Password is required')

class UserResource(Resource):

    parser.add_argument('email', type=str, required=False, help='Email is required')

    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        email = args['email']

        # Check if the username is already in use
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        existing_user = cursor.fetchone()
        conn.close()

        if existing_user:
            return {'message': 'Username already in use'}, 400

        # Create a new user in the database
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
        conn.commit()
        conn.close()

        return {'message': 'User registered successfully'}, 201


class LoginResource(Resource):
    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        # Check if the username is already in the database
        conn = sqlite3.connect('user_database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        conn.close()

        if user is None:
            return {'message': 'User not found'}, 404

        # Check if the provided password matches the stored password
        if user[2] != password:  # Assuming password is in the third column of the 'users' table
            return {'message': 'Incorrect password'}, 401

        return {'message': 'Login successful'}

api.add_resource(UserResource, '/signup')
api.add_resource(LoginResource, '/login')

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")


