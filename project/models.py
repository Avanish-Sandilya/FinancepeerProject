
from project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.Text, nullable=False, unique = True, index = True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name, password):
        self.username = name
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username: {self.username}"



class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key = True)
    userId = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)

    def __init__(self, id, userId, title, body):
        self.id = id
        self.userId = userId
        self.title = title
        self.body = body


    def __repr__(self):
        return f"Id: {self.id} userId: {self.userId} title: {self.title} body: {self.body}"
