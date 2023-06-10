from flask_jwt_extended import create_access_token
from api.models.user_note import UserNoteModel
from api.models.note import NoteModel


def test_get_notes_single_uncataloged_note(client):
    with client.application.app_context():
        token = create_access_token(identity=1)

    response = client.get(
        '/notes',
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200

    assert len(response.json['uncataloged']) == 2

    assert response.json['uncataloged'][0]['note_id'] == 1
    assert response.json['uncataloged'][0]['title'] == 'test_title'
    assert response.json['uncataloged'][0]['description'] == 'test_description'
    assert response.json['uncataloged'][0]['created_date'] == '2021-01-01 00:00:00'
    assert response.json['uncataloged'][0]['updated_date'] == '2021-01-01 00:00:00'

    assert 'body' not in response.json['uncataloged'][0]
    assert 'catalog_id' not in response.json['uncataloged'][0]

    assert response.json['catalogs'] == []


def test_get_notes_single_cataloged_and_uncataloged(client):
    with client.application.app_context():
        token = create_access_token(identity=1)
        NoteModel(title="test_title2", description="test_description2",
                  body="test_body2", created_date="2021-01-01",
                  updated_date="2021-01-01", catalog_id=1).save()
        UserNoteModel(user_id=1, note_id=2).save()

    response = client.get(
        '/notes',
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200
    assert len(response.json['uncataloged']) == 2
    assert len(response.json['catalogs']) == 1

    assert response.json['uncataloged'][0]['note_id'] == 1
    assert response.json['uncataloged'][0]['title'] == 'test_title'
    assert response.json['uncataloged'][0]['description'] == 'test_description'
    assert response.json['uncataloged'][0]['created_date'] == '2021-01-01 00:00:00'
    assert response.json['uncataloged'][0]['updated_date'] == '2021-01-01 00:00:00'

    assert 'body' not in response.json['uncataloged'][0]
    assert 'catalog_id' not in response.json['uncataloged'][0]

    assert response.json['catalogs'][0]['catalog_id'] == 1
    assert response.json['catalogs'][0]['catalog_name'] == 'test_catalog1'
    assert response.json['catalogs'][0]['notes'][0]['title'] == 'test_title2'
    assert response.json['catalogs'][0]['notes'][0]['description'] == 'test_description2'  # noqa
    assert response.json['catalogs'][0]['notes'][0]['created_date'] == '2021-01-01 00:00:00'  # noqa
    assert response.json['catalogs'][0]['notes'][0]['updated_date'] == '2021-01-01 00:00:00'  # noqa

    assert 'body' not in response.json['catalogs'][0]['notes'][0]
    assert 'catalog_id' not in response.json['catalogs'][0]['notes'][0]


def test_get_notes_multiple_cataloged_and_uncataloged(client):
    with client.application.app_context():
        token = create_access_token(identity=1)
        NoteModel(title="test_title2", description="test_description2",
                  body="test_body2", created_date="2021-01-01",
                  updated_date="2021-01-01", catalog_id=1).save()
        UserNoteModel(user_id=1, note_id=2).save()
        NoteModel(title="test_title3", description="test_description3",
                  body="test_body3", created_date="2021-01-01",
                  updated_date="2021-01-01", catalog_id=2).save()
        UserNoteModel(user_id=1, note_id=3).save()

    response = client.get(
        '/notes',
        content_type='application/json',
        headers={'Authorization': f'Bearer {token}'}
    )

    assert response.status_code == 200

    assert len(response.json['uncataloged']) == 2
    assert len(response.json['catalogs']) == 2

    assert response.json['uncataloged'][0]['note_id'] == 1

    assert response.json['catalogs'][0]['catalog_id'] == 1
    assert response.json['catalogs'][0]['catalog_name'] == 'test_catalog1'
    assert response.json['catalogs'][0]['notes'][0]['title'] == 'test_title2'

    assert response.json['catalogs'][1]['catalog_id'] == 2
    assert response.json['catalogs'][1]['catalog_name'] == 'test_catalog2'
    assert response.json['catalogs'][1]['notes'][0]['title'] == 'test_title3'
