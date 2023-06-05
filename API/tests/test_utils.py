from api.utilities.note import check_if_note_exists, get_note_by_id
from api.utilities.db_utils import check_if_user_exists
from api.utilities.user_note import get_user_note_by_note_id
from api.utilities.catalog import get_catalog_id_by_name, get_catalog_name_by_id
from api.utilities.notes import get_all_notes_of_user
from api.utilities.common import remove_dict_fields
import datetime


def test_check_if_note_exists(client, app):
    with app.app_context():
        assert check_if_note_exists(1) is True
        assert check_if_note_exists(100) is False


def test_get_note_by_id(client, app):
    with app.app_context():
        note = get_note_by_id(1)
        assert note.note_id == 1
        assert note.title == "test_title"
        assert note.description == "test_description"
        assert note.body == "test_body"
        assert note.created_date == datetime.datetime(2021, 1, 1, 0, 0)
        assert note.updated_date == datetime.datetime(2021, 1, 1, 0, 0)
        assert note.catalog_id is None

        note = get_note_by_id(100)
        assert note is None


def test_check_if_user_exists(client, app):
    with app.app_context():
        assert check_if_user_exists(1) is True
        assert check_if_user_exists(100) is False


def test_get_user_note_by_note_id(client, app):
    with app.app_context():
        user_note = get_user_note_by_note_id(1)
        assert user_note.user_id == 1
        assert user_note.note_id == 1

        user_note = get_user_note_by_note_id(100)
        assert user_note is None


def test_get_catalog_id_by_name(client, app):
    with app.app_context():
        assert get_catalog_id_by_name("test_catalog1") == 1
        assert get_catalog_id_by_name("test_catalog10") is None


def test_get_catalog_name_by_id(client, app):
    with app.app_context():
        assert get_catalog_name_by_id(1) == "test_catalog1"
        assert get_catalog_name_by_id(100) is None


def test_get_all_notes_of_user(client, app):
    with app.app_context():
        notes = get_all_notes_of_user(1)
        assert len(notes) == 1
        assert notes[0].note_id == 1
        assert notes[0].title == "test_title"
        assert notes[0].description == "test_description"
        assert notes[0].body == "test_body"
        assert notes[0].catalog_id is None

        notes = get_all_notes_of_user(100)
        assert len(notes) == 0


def test_remove_dict_fields(client, app):
    test_dict = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    }

    assert remove_dict_fields(test_dict, ["key1", "key2"]) == {
        "key3": "value3"}
