import json


def test_post(client):
    response = client.post(
        '/note',
        data=json.dumps(dict(
            user_id=1,
        )),
        content_type='application/json',
    )
    assert response.status_code == 201
    assert response.json == {"note_id": 2}

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=2,
        )),
        content_type='application/json',
    )

    assert response.status_code == 200
    assert response.json["note_id"] == 2


def test_get(client):
    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.json == {"note_id": 1, "title": "test_title",
                             "description": "test_description",
                             "body": "test_body",
                             "created_date": "2021-01-01 00:00:00",
                             "updated_date": "2021-01-01 00:00:00",
                             'catalog_id': None}


def test_put(client):
    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=1,
            title="updated title",
            description="updated description",
            body="updated body",
            catalog_id=None
        )),
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.json == {"message": "Note updated."}

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
    )

    assert response.status_code == 200
    assert response.json["note_id"] == 1
    assert response.json["title"] == "updated title"
    assert response.json["description"] == "updated description"
    assert response.json["body"] == "updated body"
    assert "created_date" in response.json
    assert "updated_date" in response.json


def test_delete(client):
    response = client.delete(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
    )
    assert response.status_code == 200
    assert response.json == {"message": "Note deleted."}

    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
    )

    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}


def test_get_404(client):
    response = client.get(
        '/note',
        data=json.dumps(dict(
            note_id=100,
        )),
        content_type='application/json',
    )
    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}


def test_post_404(client):
    response = client.post(
        '/note',
        data=json.dumps(dict(
            user_id=100,
        )),
        content_type='application/json',
    )
    assert response.status_code == 404
    assert response.json == {"message": "User not found."}

    response = client.post(
        '/note',
        data=json.dumps(dict(
            user_id=1,
            catalog_id=100
        )),
        content_type='application/json',
    )
    assert response.status_code == 404
    assert response.json == {"message": "Catalog not found."}


def test_post_400(client):
    response = client.post(
        '/note',
        data=json.dumps(dict(
            user_id="abc",
        )),
        content_type='application/json',
    )

    assert response.status_code == 400


def test_delete_404(client):
    response = client.delete(
        '/note',
        data=json.dumps(dict(
            note_id=100,
        )),
        content_type='application/json',
    )
    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}


def test_put_404(client):
    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=100,
            title="updated title",
            description="updated description",
            body="updated body",
            catalog_id=None
        )),
        content_type='application/json',
    )

    assert response.status_code == 404
    assert response.json == {"message": "Note not found."}

    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=1,
            catalog_id=100,
            title="updated title",
            description="updated description",
            body="updated body",
        )),
        content_type='application/json',
    )

    assert response.status_code == 404
    assert response.json == {"message": "Catalog not found."}


def test_put_400(client):
    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id="abc",
            title="updated title",
            description="updated description",
            body="updated body",
            catalog_id=None
        )),
        content_type='application/json',
    )

    assert response.status_code == 400

    response = client.put(
        '/note',
        data=json.dumps(dict(
            note_id=1,
        )),
        content_type='application/json',
    )

    assert response.status_code == 400
    assert response.json == {"message": "No data to update."}
