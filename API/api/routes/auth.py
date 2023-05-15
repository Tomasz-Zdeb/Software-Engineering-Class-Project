import datetime

from flask_jwt_extended import create_access_token
from flask_restx import Resource, reqparse
from sqlalchemy import or_

from api import api
from api.models.user import UserModel
from api.utilities.auth import hash_password

# Login parser

login_parser = reqparse.RequestParser()
login_parser.add_argument('email', required=True, type=str)
login_parser.add_argument('password', required=True, type=str)

# Register parser

register_parser = reqparse.RequestParser()
register_parser.add_argument(
    'name', required=True, type=str)
register_parser.add_argument('email', required=True, type=str)
register_parser.add_argument(
    'password', required=True, type=str)


@api.route('/login')
class Login(Resource):
    @api.doc(description='Login endpoint')
    @api.expect(login_parser)
    @api.doc(params={'email': 'Email', 'password': 'Password'})
    @api.response(200, 'Success')
    @api.response(403, 'Forbidden')
    def post(self):
        args = login_parser.parse_args()

        user = UserModel.query.filter_by(email=args['email']).first()

        if user is None:
            return {'message': 'Invalid email or password.'}, 403

        if user.check_password(args['password']):
            access_token = create_access_token(identity=user.user_id)
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid email or password.'}, 403


@api.route('/register')
class Register(Resource):
    @api.doc(description='Register endpoint')
    @api.expect(register_parser)
    @api.doc(params={'name': 'Username', 'email': 'Email', 'password': 'Password'})
    @api.response(200, 'Success')
    @api.response(403, 'Forbidden')
    def post(self):
        args = register_parser.parse_args()

        user = UserModel.query.filter(
            or_(UserModel.email == args['email'],
                UserModel.name == args['name'])).first()

        if user is not None:
            return {'message': 'Username or email already in use.'}, 403

        new_user = UserModel(
            name=args['name'],
            password=hash_password(args['password']),
            email=args['email'],
            created_date=datetime.datetime.now())
        new_user.save()

        return {'message': 'User created successfully.'}, 200
