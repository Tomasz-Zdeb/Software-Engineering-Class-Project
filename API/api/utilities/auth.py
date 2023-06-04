from api.models.user_note import UserNoteModel
from api import bcrypt


def user_has_permission(user_id, note_id):
    if user_id is None or note_id is None:
        return False

    user_note = UserNoteModel.query.filter_by(
        user_id=user_id, note_id=note_id).first()

    if user_note is None:
        return False

    return True


def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')
