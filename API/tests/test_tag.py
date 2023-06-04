from flask_jwt_extended import create_access_token
from api.models.tag import TagService

def test_post(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    note_id = 2
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
    assert response.json == {"message": 
                             f"Tag '{tag_name}' has been successfully created.", 
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
    
def test_get(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    note_id = 2

    response = client.get(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': note_id}
    )

    assert response.status_code == 200
    assert 'tags' in response.json

def test_get_note_tags_400(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.get(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={}
    )

    assert response.status_code == 400
    assert response.json == {
        "message": "Input payload validation failed",
        "errors": {
            "note_id": "Note ID Missing required parameter in the JSON body or the "
            "post body or the query string"
        }
    }

def test_get_note_tags_403(client):
    with client.application.app_context():
        token = create_access_token(identity=2)

    note_id = 1

    response = client.get(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': note_id}
    )

    assert response.status_code == 403
    assert response.json == {"message": "You do not have permission to view tags for"
                             " this note."}

def test_get_note_tags_404(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    note_id = 9999

    response = client.get(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'note_id': note_id}
    )

    assert response.status_code == 404
    assert response.json == {"message": f"Note with ID {note_id} not found."}

def test_delete(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    tag_id = 3

    response = client.delete(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'tag_id': tag_id}
    )

    assert response.status_code == 200
    assert response.json == {"message": 
                             f"Tag with ID {tag_id} has been successfully deleted."}
    
def test_delete_note_tags_400(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.delete(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={}
    )

    assert response.status_code == 400
    assert response.json == {
        "message": "Input payload validation failed",
        "errors": {
            "tag_id": "Tag ID Missing required parameter in the JSON body or the post "
            "body or the query string"
        }
    }

def test_delete_note_tags_403(client):
    with client.application.app_context():
        token = create_access_token(identity=2)

    tag_id = 3

    response = client.delete(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'tag_id': tag_id}
    )

    assert response.status_code == 403
    assert response.json == {"message": "You do not have permission to delete tags for "
                             "this note."}

def test_delete_note_tags_404(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    tag_id = 9999

    response = client.delete(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'tag_id': tag_id}
    )

    assert response.status_code == 404
    assert response.json == {"message": f"Tag with ID {tag_id} not found."}

def test_put_note_tags_200(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    tag_id = 3

    response = client.get(
        f'/note/{tag_id}/tags',
        headers={'Authorization': f'Bearer {token}'},
    )
    note_id = response.json['note_id']

    new_tag_name = 'updated_tag'

    response = client.put(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'tag_id': tag_id, 'tag_name': new_tag_name}
    )

    assert response.status_code == 200
    assert response.json == {"tag_id": tag_id, "note_id": note_id, 
                             "tag_name": new_tag_name}


def test_put_note_tags_400(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.put(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={}
    )

    assert response.status_code == 400
    assert response.json == {
        "message": "Input payload validation failed",
        "errors": {
            "tag_id": "Tag ID Missing required parameter in the JSON body or the post "
            "body or the query string",
            "tag_name": "Tag Name Missing required parameter in the JSON body or the "
            "post body or the query string"
        }
    }

def test_put_note_tags_403(client):
    with client.application.app_context():
        token = create_access_token(identity=2)

    tag_id = 3
    new_tag_name = 'updated_tag'

    response = client.put(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'tag_id': tag_id, 'tag_name': new_tag_name}
    )

    assert response.status_code == 403
    assert response.json == {"message": 
                             "You do not have permission to update this tag."}

def test_put_note_tags_404(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    tag_id = 9999
    new_tag_name = 'updated_tag'

    response = client.put(
        '/note/tags',
        headers={'Authorization': f'Bearer {token}'},
        json={'tag_id': tag_id, 'tag_name': new_tag_name}
    )

    assert response.status_code == 404
    assert response.json == {"message": f"Tag with ID {tag_id} not found."}
