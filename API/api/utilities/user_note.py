from api import db
from api.models.user_note import UserNoteModel


def get_user_note_by_note_id(note_id):
    user_note = db.session.query(UserNoteModel).filter_by(
        note_id=note_id).first()
    return user_note
