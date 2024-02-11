from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from model import *
from api import *


#==============================configuration===============================
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blogs.sqlite3'
api.init_app(app)
db.init_app(app)
app.app_context().push()

#==============================routes=======================================



@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/')
# def index():
#     #query all blogs
#     authors = Author.query.all()
#     return render_template('Author.html',authors=authors)


# @app.route('/get_blog/<int:blog_id>')
# def get_blog(blog_id):
#     blog = Blog.query.get(blog_id)
#     return jsonify({'id':blog.id,'title':blog.title, 'content':blog.content})


# #submit-author
# @app.route('/submit-authorapi', methods=['POST'])
# def submit_authorapi():
#     data = request.get_json()
#     a = data['authorName']
#     b = data['authorEmail']
#     author = Author(name = a, email=b)
#     db.session.add(author)
#     db.session.commit()
#     return jsonify({'message':'Author added successfully!'})


# @app.route('/submit-author', methods=['POST'])
# def submit_author():
#     a = request.form['authorName']
#     b = request.form['authorEmail']
#     author = Author(name = a, email=b)
#     db.session.add(author)
#     db.session.commit()
#     return redirect(url_for('index'))

# #delete_author/{{author.id}}
# @app.route('/delete_author/<int:author_id>')
# def delete_author(author_id):
#     author = Author.query.get(author_id)
#     blogs = author.blog_relation
#     for blog in blogs:
#         asso = Association.query.filter_by(blog_id=blog.id).first()
#         db.session.delete(asso)
#         db.session.delete(blog)
#     db.session.delete(author)
#     db.session.commit()
#     return redirect(url_for('index'))


# #edit_author/{{author_id}}
# @app.route('/edit_author/<int:author_id>', methods=['POST'])
# def edit_author(author_id):
#     a = request.form['authorName']
#     b = request.form['authorEmail']
#     Author.query.filter_by(id=author_id).update({'name':a, 'email':b})
#     db.session.commit()
#     return redirect(url_for('index'))


# #Blogs/{{author.id}}
# @app.route('/blogs/<int:author_id>')
# def blogs(author_id):
#     author = Author.query.get(author_id)
#     blogs = author.blog_relation
#     return render_template('Blog.html', blogs=blogs, author=author)

# #/submit-blog/{{author.id}}
# @app.route('/submit-blog/<int:author_id>', methods=['POST'])
# def submit_blog(author_id):
#     a = request.form['blogTitle']
#     b = request.form['blogContent']
#     blog = Blog(title = a, content=b, author_id=author_id)
#     db.session.add(blog)
#     db.session.commit()

#     blog = Blog.query.filter_by(title=a, content=b ).first()
#     bid = blog.id

#     association = Association(blog_id=bid, author_id=author_id)
#     db.session.add(association)
#     db.session.commit()
#     return redirect(url_for('index'))

# #delete_blog/{{blog.id}}
# @app.route('/delete_blog/<int:blog_id>')
# def delete_blog(blog_id):
#     blog = Blog.query.get(blog_id)
#     asso = Association.query.filter_by(blog_id=blog_id).first()
#     db.session.delete(asso)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect(url_for('blogs', author_id=asso.author_id))

# #/edit_blog/{{blog.id}}/{{author.id}}
# @app.route('/edit_blog/<int:blog_id>', methods=['POST'])
# def edit_blog(blog_id):
#     a = request.form['blogTitle']
#     b = request.form['blogContent']
#     Blog.query.filter_by(id=blog_id).update({'title':a, 'content':b})
#     db.session.commit()
#     asso = Association.query.filter_by(blog_id=blog_id).first()
#     return redirect(url_for('blogs', author_id=asso.author_id))


# /submit-blog
# @app.route('/submit-blog', methods=['POST'])
# def submit_blog():
#     a = request.form['blogTitle']
#     b = request.form['blogContent']
#     blog = Blog(title = a, content=b)
#     db.session.add(blog)
#     db.session.commit()
#     return redirect(url_for('index'))

# #delete_blog/{{blog.id}}
# @app.route('/delete_blog/<int:blog_id>')
# def delete_blog(blog_id):
#     blog = Blog.query.get(blog_id)
#     db.session.delete(blog)
#     db.session.commit()
#     return redirect(url_for('index'))

# #edit_blog/{{blog.id}}
# @app.route('/edit_blog/<int:blog_id>', methods=['POST'])
# def edit_blog(blog_id):
#     a = request.form['blogTitle']
#     b = request.form['blogContent']
#     Blog.query.filter_by(id=blog_id).update({'title':a, 'content':b})
#     db.session.commit()
#     return redirect(url_for('index'))
    















if __name__ == "__main__":
    app.run(debug=True)