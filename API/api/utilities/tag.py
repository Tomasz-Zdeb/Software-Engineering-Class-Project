from .note import NoteModel
    
def owns_note(self, note_id):
    note = NoteModel.query.get(note_id)
    if note is None:
        return False
    return note.user_id == self.id