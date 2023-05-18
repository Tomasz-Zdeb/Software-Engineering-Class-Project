from api import jwt


@jwt.unauthorized_loader
def unauthorized_response(reason):
    return {'message': 'Missing authorization header.'}, 401


@jwt.expired_token_loader
def expired_token_response(jwt_header, jwt_payload):
    return {'message': 'Token has expired.'}, 401


@jwt.invalid_token_loader
def invalid_token_response(reason):
    return {'message': 'Invalid token.'}, 422
