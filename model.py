from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

#Blog model


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    blog_relation = db.relationship('Blog', backref='author', secondary="association")


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)


class Association(db.Model):
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), primary_key=True, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True, nullable=False)




