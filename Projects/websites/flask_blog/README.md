# Flask Blog App

This is a very simple application for creating and displaying blog posts.

## Getting Started

### What you need to know already

To do this project you need to understand:

- Flask basics (see the [Flask calculator project](../flask_calculator)).

### What we are introducing in this project

This project focuses on teaching you about:

- Basic Databases with SQLAlchemy

### Project Requirements

There are two packages we need to `pip install` for this project to work.

They are:

- Flask
- flask_sqlalchemy

The following command should install them for you:

`pip install flask flask_sqlalchemy`

Flask is used for building the website whereas SQLAlchemy is used for 
storing the data for the blog posts.


## The Lesson

### Databases

In most real world programs we have to deal with data. Data can be anything
but it is usually seen as text or numbers stored in some way. This can held 
in a text file, a spreadsheet, on the internet. But for websites most data
is stored inside a database.

### What are databases?

We won't cover this in depth but it's important to understand that databases
are made of "tables", like in a spreadsheet. These tables have columns which
have names and types (for example a column could be called "names" and have
the type of string).

### How do we access the data in databases?

There are many way to access data inside a database, often involving another
language called SQL.

We use an ORM called SQLAlchemy which allows us to access everything in python.

When you access data in a database you say you `query` the database.

When you add something to a database you say you `insert` a record into the 
database.

When you change something in a database you say you `update` the database.

## The Project

### Step 1 - Setting up the Database

#### Step 1a - adding the database location
Create a file called `blog.py`. It's opening contents should contain:

```python
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)
``` 

This imports everything we need for our application and tells our application
where the database will be. In this case we are using an sqlite database
which will be called `blog.db` and is going to be located in the same folder
as this project.

We then create an `SQLAlchemy` instance and call it `db` - this is what we
will use to access our database.

But before we actualy make the database we have to create the table to store 
our blog posts in. We call this database modelling and therefore will make a 
database model to do this for us.

#### Step 1b - modelling the blog posts table.

Add the following to the code:

```python
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True, nullable=False)
    content = db.Column(db.Text(), nullable=False)
```

This is a SQLAlchemy database model.

It's a simple class which inherits from `db.Model` and then defines several
columns within itself.

We call these columns `id`, `title` and `content`. These are what they will 
be called in the table as well.

The title column will hold the post title, the content column holds the posts
content. The id column is a special column we will use to query the database.

The `unique` argument, if true, indicates that no two posts can have the 
same data in this column.

The `nullable` argument, if false, indicates that a column must have data in
it and cannot be blank. 

The `primary_key` argument is a special argument indicating the column is
a unique column which you can easily query the data by. It makes the column
both unique and not nullable by default.  


#### Step 1c - creating the database

At the bottom of the file add a `main` block like so:

```python
if __name__ == '__main__':
    db.create_all()
```

Now run the file with:

```bash
python blog.py
```

This creates the database and the tables within it. Now in your folder you
should have a `blog.db` file. This is your database.

### Step 2 - creating the home page and listing the posts.

We're going to create a home page which lists all the blog posts.

Create a folder called `templates` and within it a file called
`blog-list.html`.

The file should contain the following:

```jinja2
<!doctype html>

<title>My Blog</title>


<h1>Welcome to my blog! Find my posts below</h1>

<div>
    <ul>
        {% for post in posts %}
            <li><a href="{{ url_for('view_post', pk=post.id) }}">{{ post.title }}</a></li>
        {% endfor %}
    </ul>
</div>
```

This creates a page with a title which, if any exist, will list out
all the blog posts.

Add the following function to `blog.py` to match this template:

```python
@app.route('/')
def home():
    return render_template('blog-list.html', posts=BlogPost.query.all())
```

This creates a home page which renders the template with a list of all
our blog posts.

Note how we use the `BlogPost` model and run the `query` method off of it.

`query.all()` gets all of the records we have in the database - currently none.

### Step 3 - creating a blog post

Let's add a simple form to create a post with.

Create a new HTML file called `create-post.html` in the template folder.

The file should look like:

```jinja2
<!DOCTYPE html>
<title>Write a blog post!</title>

<h1>Write a blog post</h1>

<form action="{{ url_for('create_post') }}" method="post">

    <label for="title">Title</label>
    <input name="title" id="title" placeholder="Title..." required />
    <br>
    <br>
    <label for="content">Content</label>
    <textarea name="content" id="content"required>
    </textarea>
    <br>
    <br>
    <button type="submit">Submit</button>
</form>
``` 

Here we've created a form which sends data to a `create_post` function 
(which we make next).

It has two input fields, title and content - these relate exactly to our
database columns `title` and `content`. We don't need to provide `id` as 
this is made for us automatically.

Let's make a function to match this view:

```python
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        new_post = BlogPost(title=request.form['title'], content=request.form['content'])
        db.session.add(new_post)
        db.session.commit()
        return home()

    return render_template('create-post.html')
```

This function uses the `GET` and `POST` method. We check which method has 
been used, if it is `POST` that means a form has been submitted and we
want to make a new post. Otherwise we just want to see the form.

If it is a `POST` request we create a new post using the form data we have.
We add this to the db session and then commit it. Commiting in database
terms is the equivalent to saving a document. At this point we've put a new
post in our database and we return to the home page.

Let's add a link to this page on our home page. Add the following to the bottom
of `blog-list.html`:

```jinja2
<div>
    Create a new post <a href="{{ url_for('create_post') }}">here</a>.
</div>
``` 

### Step 3 - viewing a post

Now we can list posts and make them we finally need to view them.

Let's make one more html template, call it `blog-post.html`.

This one will be very simple:

```jinja2
<!doctype html>

<title>{{ post.title }}</title>

<h1>{{ post.title }}</h1>
<br>
<div>
    {{ post.content }}
</div>
```

As we can see we are expecting a post, and all we do is display
the title and content.

Make the function to match in `blog.py`:

```python
@app.route('/posts/<int:pk>')
def view_post(pk):
    return render_template('blog-post.html', post=BlogPost.query.get(pk))
```
This one takes an argument for the primary key (pk or id) of a post
and uses `query.get(pk)` to find the post we want. It then sends this to
our new template and renders it.

That is it. At this point the site should be fully functional.

### Step 4 - running the site.

Open a terminal in your folder and run:

```bash
export FLASK_APP=blog.py
flask run
```

In a browser go to [localhost:5000](localhost:5000) and your site should be
there. Try to create a page and see if you can visit it.

## Next

Think about what else you may want to add to a blog page.

What else could you add to the model and how could you display it?

What if you wanted to search for articles? You can use `query.filter_by` 
for that.

Do you know HTML and CSS? Why not try style your blog page a bit.