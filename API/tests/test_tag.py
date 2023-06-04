from flask_jwt_extended import create_access_token
from ..api.models.tag import TagService

def test_post(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    note_id = 1
    tag_name = 'new_tag'

    response = client.post(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': note_id, 'tag_name': tag_name}
    )

    assert response.status_code == 201
    assert 'tag_id' in response.json

    response = client.get(
        f'/note/{note_id}/tags',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert tag_name in [tag['tag_name'] for tag in response.json]
    assert 'tag_id' in response.json
    assert response.json == {"message": f"Tag '{tag_name}' has been successfully created.", 
                             "tag_id": response.json['tag_id']}

def test_post_400(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.post(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': None, 'tag_name': 'new_tag'}
    )

    response = client.post(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': None, 'tag_name': 'test_tag'}
    )

    assert response.status_code == 400
    assert response.json == {"message": "Invalid request body. Ensure that note_id and "
                             "tag_name are present and in the correct format."}


def test_post_403(client):
    with client.application.app_context():
        token = create_access_token(identity=2)

    note_id = 1
    tag_name = 'new_tag'

    response = client.post(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': note_id, 'tag_name': tag_name}
    )

    assert response.status_code == 403
    assert response.json == {"message": "You do not have permission to create tags for"
                             " this note."}


def test_post_404(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    note_id = 100
    tag_name = 'new_tag'

    response = client.post(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': note_id, 'tag_name': tag_name}
    )

    assert response.status_code == 404
    assert response.json == {"message": 
                             f"Note with ID {note_id} not found."}


def test_post_422(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.post(
        '/note/tags',
        headers={'Authorization': 'Bearer abc'},
        json={'note_id': 1, 'tag_name': 'new_tag'}
    )

    response = client.post(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': "invalid", 'tag_name': 'test_tag'}
    )

    assert response.status_code == 422

def test_post_note_tags_500_internal_error(client, monkeypatch):
    def mock_create_tag(note_id, tag_name):
        raise Exception("Database error")

    monkeypatch.setattr(TagService, "create_tag", mock_create_tag)

    with client.application.app_context():
        token = create_access_token(identity=1)

    note_id = 1
    tag_name = 'new_tag'
    response = client.post('/note/tags', headers={'Authorization': f'Bearer {token}'}, 
                           json={'note_id': note_id, 'tag_name': tag_name})

    assert response.status_code == 500
    assert response.json == {"message": "An error occurred while creating the tag. "
                             "Please try again."}