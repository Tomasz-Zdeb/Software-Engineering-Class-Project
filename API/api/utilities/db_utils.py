"""
This is a temporary module that defines some required functions for the /note endpoint to work.
It should be removed once the /user and /catalog endpoints are implemented.
"""

from api import db
from api.models.catalog import CatalogModel
from api.models.user import UserModel


def check_if_user_exists(user_id):
    exists = db.session.query(UserModel.user_id).filter_by(
        user_id=user_id).scalar() is not None
    return exists


def check_if_catalog_exists(catalog_id):
    exists = db.session.query(CatalogModel.catalog_id).filter_by(
        catalog_id=catalog_id).scalar() is not None
    return exists
