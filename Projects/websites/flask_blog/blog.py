from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text(), nullable=False)


@app.route('/')
def home():
    return render_template('blog-list.html', posts=BlogPost.query.all())


@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        new_post = BlogPost(title=request.form['title'], content=request.form['content'])
        db.session.add(new_post)
        db.session.commit()
        return home()

    return render_template('create-post.html')


@app.route('/posts/<int:pk>')
def view_post(pk):
    return render_template('blog-post.html', post=BlogPost.query.get(pk))


if __name__ == '__main__':
    db.create_all()
