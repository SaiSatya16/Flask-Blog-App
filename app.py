from flask import Flask, render_template, request, redirect, url_for, flash, session
from model import *


#==============================configuration===============================
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Blogs.sqlite3'
db.init_app(app)
app.app_context().push()

#==============================routes=======================================

@app.route('/')
def index():
    #query all blogs
    b = Blog.query.all()
    return render_template('index.html', blogs=b)

# /submit-blog
@app.route('/submit-blog', methods=['POST'])
def submit_blog():
    a = request.form['blogTitle']
    b = request.form['blogContent']
    blog = Blog(title = a, content=b)
    db.session.add(blog)
    db.session.commit()
    return redirect(url_for('index'))

#delete_blog/{{blog.id}}
@app.route('/delete_blog/<int:blog_id>')
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('index'))















if __name__ == "__main__":
    app.run(debug=True)