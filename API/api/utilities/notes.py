from api import db
from api.models.note import NoteModel
from api.models.user_note import UserNoteModel


def get_all_notes_of_user(user_id):
    return (
        db.session.query(NoteModel)
        .join(UserNoteModel)
        .filter(UserNoteModel.user_id == user_id)
        .all()
    )
