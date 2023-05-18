import os

import pytest

from api.models.note import NoteModel
from api.models.user import UserModel
from api.models.user_note import UserNoteModel


@pytest.fixture()
def app():
    os.environ["TESTING"] = "True"

    from api import app, db

    # Initial setup
    with app.app_context():
        db.create_all()
        UserModel(name="test_user", password="test_pass",
                  created_date="2021-01-01", email="test_email").save()
        NoteModel(title="test_title", description="test_description",
                  body="test_body", created_date="2021-01-01",
                  updated_date="2021-01-01").save()
        UserNoteModel(user_id=1, note_id=1).save()

    yield app

    # Cleanup
    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()
