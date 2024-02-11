from flask_restful import Resource, Api, reqparse, fields, marshal_with
from model import *
import json
from flask import make_response
import os

api = Api()

#==============================output fields========================================
author_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

blog_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'content': fields.String,
    'author_id': fields.Integer
}

#====================Create Author and Blog request pares=======================================

create_author_parser = reqparse.RequestParser()
create_author_parser.add_argument('authorName')
create_author_parser.add_argument('authorEmail')

create_blog_parser = reqparse.RequestParser()
create_blog_parser.add_argument('title')
create_blog_parser.add_argument('content')
create_blog_parser.add_argument('author_id')

#====================Update Author and Blog request pares=======================================

update_author_parser = reqparse.RequestParser()
update_author_parser.add_argument('authorName')
update_author_parser.add_argument('authorEmail')

update_blog_parser = reqparse.RequestParser()
update_blog_parser.add_argument('title')
update_blog_parser.add_argument('content')
update_blog_parser.add_argument('author_id')

#=================================Author api======================================================

class AuthorApi(Resource):
    
    def get(self):
        data = []
        authors = Author.query.all()
        for author in authors:
            data.append({'id':author.id, 'name':author.name, 'email':author.email})
        return data
    
        
    
    @marshal_with(author_fields)
    def post(self):
        data = create_author_parser.parse_args()
        author = Author(name = data['authorName'], email=data['authorEmail'])
        db.session.add(author)
        db.session.commit()
        return author

    def delete(self, author_id):
        author = Author.query.get(author_id)
        blogs = author.blog_relation
        for blog in blogs:
            asso = Association.query.filter_by(blog_id=blog.id).first()
            db.session.delete(asso)
            db.session.delete(blog)
        db.session.delete(author)
        db.session.commit()
        return {'message':'Author deleted successfully!'}

    @marshal_with(author_fields)
    def put(self, author_id):
        data = update_author_parser.parse_args()
        Author.query.filter_by(id=author_id).update({'name':data['authorName'], 'email':data['authorEmail']})
        db.session.commit()
        return Author.query.get(author_id)
    

#=================================Blog api======================================================
class BlogApi(Resource):
    def get(self):
        data = []
        blogs = Blog.query.all()
        for blog in blogs:
            data.append({'id':blog.id, 'title':blog.title, 'content':blog.content, 'author_id':blog.author_id})
        return data

    @marshal_with(blog_fields)
    def post(self):
        data = create_blog_parser.parse_args()
        blog = Blog(title = data['title'], content=data['content'], author_id=data['author_id'])
        db.session.add(blog)
        db.session.commit()
        return blog

    def delete(self, blog_id):
        blog = Blog.query.get(blog_id)
        db.session.delete(blog)
        db.session.commit()
        return {'message':'Blog deleted successfully!'}

    @marshal_with(blog_fields)
    def put(self, blog_id):
        data = update_blog_parser.parse_args()
        Blog.query.filter_by(id=blog_id).update({'title':data['title'], 'content':data['content'], 'author_id':data['author_id']})
        db.session.commit()
        return Blog.query.get(blog_id)
    
api.add_resource(AuthorApi, '/author/<int:author_id>', '/author')
api.add_resource(BlogApi, '/blog/<int:blog_id>', '/blog')
    



