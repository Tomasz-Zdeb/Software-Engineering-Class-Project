from api import db


class CatalogModel(db.Model):
    __tablename__ = 'catalog'
    catalog_id = db.Column(db.Integer, primary_key=True)
