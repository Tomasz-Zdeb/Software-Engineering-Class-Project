from api import db
from api.utilities.auth import hash_password


class UserModel(db.Model):
    __tablename__ = 'user_table'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    password = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.Text)
    enabled = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "password": self.password,
            "created_date": self.created_date,
            "email": self.email,
            "enabled": self.enabled
        }

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.user_id

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def check_password(self, password):
        return self.password == hash_password(password)
