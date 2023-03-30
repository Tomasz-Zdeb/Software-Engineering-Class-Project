from api import api
from flask_restx import Resource, reqparse

parser = reqparse.RequestParser()
parser.add_argument('message',
                    type=str,
                    default='world',
                    help='A message to display')


@api.route('/hello')
@api.expect(parser)
@api.doc(description='An example endpoint.')
class HelloWorld(Resource):
    def get(self):
        args = parser.parse_args()
        return {'hello': args['message']}
