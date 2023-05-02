from time import strftime

from api import db


class NoteModel(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer, primary_key=True)
    catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.catalog_id'))
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    body = db.Column(db.String(100))
    created_date = db.Column(db.DateTime, nullable=False)
    updated_date = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            "note_id": self.note_id,
            "catalog_id": self.catalog_id,
            "title": self.title,
            "description": self.description,
            "body": self.body,
            "created_date": strftime("%Y-%m-%d %H:%M:%S",
                                     self.created_date.timetuple()),
            "updated_date": strftime("%Y-%m-%d %H:%M:%S",
                                     self.updated_date.timetuple())
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.note_id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, modified_note_fields):
        for key, value in modified_note_fields.items():
            setattr(self, key, value)
        self.updated_date = strftime("%Y-%m-%d %H:%M:%S")
        db.session.commit()
