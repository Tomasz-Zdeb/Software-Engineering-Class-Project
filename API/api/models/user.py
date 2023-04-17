from api import db


class UserModel(db.Model):
    __tablename__ = 'user_table'
    user_id = db.Column(db.Integer, primary_key=True)
