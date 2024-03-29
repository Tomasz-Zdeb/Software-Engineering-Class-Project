from api import db


class CatalogModel(db.Model):
    __tablename__ = 'catalog'
    catalog_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.catalog_id
