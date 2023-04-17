from api import db


class UserNoteModel(db.Model):
    __tablename__ = 'user_note'
    user_note_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user_table.user_id'))
    note_id = db.Column(db.Integer, db.ForeignKey(
        'note.note_id'))

    def to_dict(self):
        return {
            "user_note_id": self.user_note_id,
            "user_id": self.user_id,
            "note_id": self.note_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
