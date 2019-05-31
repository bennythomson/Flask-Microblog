from blog import db
from werkzeug.security import generate_password_hash, check_password_hash


class Post(db.Model):

    ''' db model for each post'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    body = db.Column(db.String(200))

    def __repr__(self):
        return self.name


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    display_name = db.Column(db.String(100))
    password_hash = db.Column(db.Text())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def __repr__(self):
        return self.name
