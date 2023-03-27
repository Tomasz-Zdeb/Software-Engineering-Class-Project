from api import api
from flask_restx import Resource


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
