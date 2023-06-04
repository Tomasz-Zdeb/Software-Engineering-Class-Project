from api import db
from api import bcrypt


class UserModel(db.Model):
    __tablename__ = 'user_table'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.Text)
    enabled = db.Column(db.Integer, default=0)
    hashed_password = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "created_date": self.created_date,
            "email": self.email,
            "enabled": self.enabled,
            "hashed_password": self.hashed_password,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.user_id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hashed_password, password)
