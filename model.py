from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#Blog model
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # def __init__(self, title, content):
    #     self.title = title
    #     self.content = content