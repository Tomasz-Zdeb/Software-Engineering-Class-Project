from api import db

class TagModel(db.Model):
    __tablename__ = 'tag'

    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {
            "tag_id": self.tag_id,
            "name": self.name
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self, tag_name):
        self.name = tag_name
        db.session.commit()


class NoteTagModel(db.Model):
    __tablename__ = 'note_tag'

    note_tag_id = db.Column(db.Integer, primary_key=True)
    note_id = db.Column(db.Integer, db.ForeignKey('note.note_id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.tag_id'))

    def to_dict(self):
        return {
            "note_tag_id": self.note_tag_id,
            "note_id": self.note_id,
            "tag_id": self.tag_id
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class TagService:
    @staticmethod
    def create_tag(note_id, tag_name):
        try:
            new_tag = TagModel(name=tag_name)
            db.session.add(new_tag)
            db.session.commit()

            new_note_tag = NoteTagModel(note_id=note_id, tag_id=new_tag.tag_id)
            db.session.add(new_note_tag)
            
            db.session.commit()

            return new_tag
        except Exception as e:
            print(e)
            db.session.rollback()
            raise

    @staticmethod
    def get_existing_tag(note_id, tag_name):
        return db.session.query(TagModel).join(NoteTagModel).filter(
            NoteTagModel.note_id == note_id, TagModel.name == tag_name).first()
