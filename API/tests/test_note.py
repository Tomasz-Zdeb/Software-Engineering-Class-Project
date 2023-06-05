import json
from flask_jwt_extended import create_access_token
from datetime import timedelta
import time


def test_post(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.post(
        '/note',
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 201
    assert response.json == {"note_id": 2}

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=2,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    assert response.json["note_id"] == 2


def test_get(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.get(
        '/note',
        headers={'Authorization': f'Bearer {token}'},
        query_string={'note_id': 2}
    )
    
    assert response.status_code == 200
    assert response.json == {
        "note_id": 2,
        "title": "titletest2",
        "description": "desctest2",
        "body": "bodytest2",
        "created_date": "2023-03-05 02:00:00",
        "updated_date": "2023-03-05 03:00:00",
        "tags": [
            {
            "tag_id": 3,
            "tag_name": "tagtest3"
            }
        ],
        "catalog_name": None
    }


def test_put(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=1,
            title="updated title",
            description="updated description",
            body="updated body",
            catalog_name=None
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 200
    assert response.json == {"message": "Note updated."}

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    assert response.json["note_id"] == 1
    assert response.json["title"] == "updated title"
    assert response.json["description"] == "updated description"
    assert response.json["body"] == "updated body"
    assert "created_date" in response.json
    assert "updated_date" in response.json


def test_delete(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.delete(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 200
    assert response.json == {"message": "Note deleted."}

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}


def test_get_404(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=100,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}


def test_post_404(client):
    with client.application.app_context():
        invalid_user_token = create_access_token(identity=100)

    response = client.post(
        '/note',
        content_type='application/json',
        headers={'Authorization': f'Bearer {invalid_user_token}'}
    )
    assert response.status_code == 404
    assert response.json == {"message": "User not found."}


def test_delete_404(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.delete(
        '/note',
        data=json.dumps(dict(
            note_id=100,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}


def test_put_404(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=100,
            title="updated title",
            description="updated description",
            body="updated body",
            catalog_name=None
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}


def test_put_400(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id="abc",
            title="updated title",
            description="updated description",
            body="updated body",
            catalog_name=None
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 400

    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 400
    assert response.json == {"message": "No data to update."}


def test_get_401(client):
    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
    )
    assert response.status_code == 401
    assert response.json == {"message": "Missing authorization header."}


def test_get_422(client):
    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': 'Bearer abc'}
    )
    assert response.status_code == 422
    assert response.json == {"message": "Invalid token."}


def test_get_403(client):
    with client.application.app_context():
        token = create_access_token(identity=2)

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )
    assert response.status_code == 403
    assert response.json == {"message": "Forbidden."}


def test_get_401_expired(client):
    with client.application.app_context():
        token = create_access_token(
            identity=1, expires_delta=timedelta(microseconds=1))

    # Sleep for 2 microseconds to ensure the token has expired.
    time.sleep(0.000002)

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 401
    assert response.json == {"message": "Token has expired."}


def test_post_401(client):
    response = client.post(
        '/note',
        content_type='application/json',
    )
    assert response.status_code == 401
    assert response.json == {"message": "Missing authorization header."}


def test_post_422(client):
    response = client.post(
        '/note',
        content_type='application/json',
        headers={'Authorization': 'Bearer abc'}
    )
    assert response.status_code == 422
    assert response.json == {"message": "Invalid token."}


def test_post_401_expired(client):
    with client.application.app_context():
        token = create_access_token(
            identity=1, expires_delta=timedelta(microseconds=1))

    time.sleep(0.000002)

    response = client.post(
        '/note',
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 401
    assert response.json == {"message": "Token has expired."}


def test_put_401(client):
    response = client.put(
        '/note',
        content_type='application/json',
    )
    assert response.status_code == 401
    assert response.json == {"message": "Missing authorization header."}


def test_put_401_expired(client):
    with client.application.app_context():
        token = create_access_token(
            identity=1, expires_delta=timedelta(microseconds=1))

    time.sleep(0.000002)

    response = client.put(
        '/note',
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 401
    assert response.json == {"message": "Token has expired."}


def test_put_422(client):
    response = client.put(
        '/note',
        content_type='application/json',
        headers={'Authorization': 'Bearer abc'}
    )

    assert response.status_code == 422
    assert response.json == {"message": "Invalid token."}


def test_put_403(client):
    with client.application.app_context():
        token = create_access_token(identity=2)

    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=1,
            title="updated title",
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 403
    assert response.json == {"message": "Forbidden."}


def test_delete_401(client):
    response = client.delete(
        '/note',
        content_type='application/json',
    )
    assert response.status_code == 401
    assert response.json == {"message": "Missing authorization header."}


def test_delete_401_expired(client):
    with client.application.app_context():
        token = create_access_token(
            identity=1, expires_delta=timedelta(microseconds=1))

    time.sleep(0.000002)

    response = client.delete(
        '/note',
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 401
    assert response.json == {"message": "Token has expired."}


def test_delete_422(client):
    response = client.delete(
        '/note',
        content_type='application/json',
        headers={'Authorization': 'Bearer abc'}
    )

    assert response.status_code == 422
    assert response.json == {"message": "Invalid token."}


def test_delete_403(client):
    with client.application.app_context():
        token = create_access_token(identity=2)

    response = client.delete(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 403
    assert response.json == {"message": "Forbidden."}
