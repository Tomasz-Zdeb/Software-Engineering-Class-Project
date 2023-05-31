from api.utilities.note import check_if_note_exists, get_note_by_id
from api.utilities.db_utils import check_if_user_exists
from api.utilities.user_note import get_user_note_by_note_id
from api.utilities.catalog import get_catalog_id_by_name, get_catalog_name_by_id
from api.models.catalog import CatalogModel
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
        CatalogModel(
            name="test_catalog",
            created_date=datetime.datetime(2021, 1, 1, 0, 0)
        ).save()
        assert get_catalog_id_by_name("test_catalog") == 1
        assert get_catalog_id_by_name("test_catalog_2") is None


def test_get_catalog_name_by_id(client, app):
    with app.app_context():
        CatalogModel(
            name="test_catalog",
            created_date=datetime.datetime(2021, 1, 1, 0, 0)
        ).save()
        assert get_catalog_name_by_id(1) == "test_catalog"
        assert get_catalog_name_by_id(100) is None
