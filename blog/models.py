from blog import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    body = db.Column(db.String(200))

    def __repr__(self):
        return self.name
