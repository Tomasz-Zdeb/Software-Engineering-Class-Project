import json
from api.models.user import UserModel


def test_login(client):
    response = client.post(
        '/login',
        data=json.dumps({
            'email': 'test_email',
            'password': 'test_pass'
        }),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert 'access_token' in response.json


def test_login_400_no_password(client):
    response = client.post(
        '/login',
        data=json.dumps({
            'email': 'test_email',
            'password': ''
        }),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert 'access_token' not in response.json
    assert response.json['message'] == 'Username, email and password required.'


def test_login_400_no_email(client):
    response = client.post(
        '/login',
        data=json.dumps({
            'email': '',
            'password': 'test_pass'
        }),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert 'access_token' not in response.json
    assert response.json['message'] == 'Username, email and password required.'


def test_register_400_no_name(client):
    response = client.post(
        '/register',
        data=json.dumps({
            'name': '',
            'email': 'test_email2',
            'password': 'test_pass2'
        }),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message'] == 'Username, email and password required.'


def test_register_400_no_email(client):
    response = client.post(
        '/register',
        data=json.dumps({
            'name': 'test_user2',
            'email': '',
            'password': 'test_pass2'
        }),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message'] == 'Username, email and password required.'


def test_register_400_no_password(client):
    response = client.post(
        '/register',
        data=json.dumps({
            'name': 'test_user2',
            'email': 'test_email2',
            'password': ''
        }),
        content_type='application/json'
    )

    assert response.status_code == 400
    assert response.json['message'] == 'Username, email and password required.'


def test_login_403(client):
    response = client.post(
        '/login',
        data=json.dumps({
            'email': 'test_email',
            'password': 'wrong_pass'
        }),
        content_type='application/json'
    )

    assert response.status_code == 403
    assert 'access_token' not in response.json
    assert response.json['message'] == 'Invalid email or password.'


def test_login_403_no_user(client):
    response = client.post(
        '/login',
        data=json.dumps({
            'email': 'wrong_email',
            'password': 'test_pass'
        }),
        content_type='application/json'
    )

    assert response.status_code == 403
    assert 'access_token' not in response.json
    assert response.json['message'] == 'Invalid email or password.'


def test_register(client):
    response = client.post(
        '/register',
        data=json.dumps({
            'name': 'test_user2',
            'email': 'test_email2',
            'password': 'test_pass2'
        }),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.json['message'] == 'User created successfully.'

    with client.application.app_context():
        user = UserModel.query.filter_by(email='test_email2').first()
        assert user is not None
        assert user.name == 'test_user2'
        assert user.email == 'test_email2'
        assert user.check_password('test_pass2') is True


def test_register_403(client):
    response = client.post(
        '/register',
        data=json.dumps({
            'name': 'test_user',
            'email': 'test_email',
            'password': 'test_pass'
        }),
        content_type='application/json'
    )

    assert response.status_code == 403
    assert response.json['message'] == 'Username or email already in use.'
