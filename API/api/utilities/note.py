from api import db
from api.models.note import NoteModel


def get_note_by_id(note_id):
    note = db.session.query(NoteModel).filter_by(note_id=note_id).first()
    return note


def check_if_note_exists(note_id):
    exists = db.session.query(NoteModel.note_id).filter_by(
        note_id=note_id).scalar() is not None
    return exists
