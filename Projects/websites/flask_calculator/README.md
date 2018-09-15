# Flask Calculator App

Contrary to the name this project has nothing to do with flasks or drinking.
We will be building a website instead, using a package called "Flask".

We're going to make this website act like a calculator.

## Getting Started

### What you need to know already

To do this project you need to understand:

- Dictionaries.
- if statements.
- Functions.
- 3rd party modules (pip).

### What we are introducing in this project

This project focuses on teaching you about:

- HTTP response/request flow.
- Decorators (briefly).
- Requests
- Flask

### Project Requirements

There are two packages we need to `pip install` for this project to work.

They are:

- Flask
- Requests

The following command should install them for you:

`pip install flask requests`

Flask we will use for building the actual website. Requests we will use for debugging.

## The Project

### Step 1 - Home Page

Create a file called `calaculator.py`. It's opening contents should contain:

```python
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to my calculator app.'
```

In the command line run the following ($ denotes beginning of the line, 
do not actally type the $):

```bash
$ export FLASK_APP=calculator.py
$ flask run
```

Open chrome with the above still running and go to the website `localhost:5000`.

You should see the text you wrote in the home function. 

#### What have we done?

We have imported `flask` and created a `Flask` object called `app`. This is the `root` of 
the website which essentially controls everything in the website and 
decides what is shown.

We don't need to understand exactly how this works now - we just need to know
how to use it.

The simplest way to use it is as a decorator. These are special objects you put
on top of functions using the `@` sign. In our project we did it like so:

```pythonstub
@app.route('/')
def home():
    return 'Welcome to my calculator app.'
```

The `@app.route('/')` is the actual decorating line. 

Decorators "wrap" a function. This means they can change how a function behaves.
In this case we change how the function behaves by attaching it to our website.

the `.route` portion of the decorator means we are declaring a website "route", 
this is the equivalent to a `URL`, i.e. the characters you put in your browsers 
address bar. `/` is the home route. e.g. when there is nothing after the website
name.

By decorating the function with this route we are saying that we want our home page
to show the content which the function returns.

To see the app we went to `localhost:5000`. This is because, as you currently 
don't have a name for your website (names cost money) we use your computers 
default name for itself `localhost`. We specifically also looked at port 5000 
(the `:5000` part of the url), which is what flask uses by default (most website
 use port 80). A port is just a place where you computer transmits information.
 
#### Extra ideas

Try make some other text in the function and display it on the website.

E.g. if you've done the random food generator project you can make it output that.

### Step 2 - Taking Arguments

After your `home` route put in the following:

```python
@app.route('/number/<int:number_to_show>')
def show_number(number_to_show):
    return 'You asked for the number {}'.format(number_to_show)
```

Run the flask app again and go to your browser.

This time go to `localhost:5000/number/2`. You should see "You asked for the 
number 2" on screen.

Try put some other numbers in the URL and see what you get. 

#### What have we done?

We've created a new route. But this time we've used something other than `/`.
This time we're saying that the url should be `/number/` and then we've added
some special syntax on the end like so `<int:number>`. 

The `<>` means our function will accept an `argument`, the bit before the `:`
colon tells us what `type` the argument is, in this case an `int`. The bit 
after the `:` tells us what the argument should be called. In this case 
`number_to_show`.

We then use this argument in our function to change wha we are saying - and
show the number.

#### Extra ideas

Try to change the url name to something else that you want.

### Step 3 - Adding Numbers

Let's use what we've learnt to do make this website do some addition.

Copy the following:

```python
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    return str(num1 + num2)
```

Restart the app, go to the browser and go to: `localhost:5000/add/1/3`

You should get 4, try out some other numbers and see if they're correct.

#### What have we done?

We've learnt we can take multiple arguments using different parts of the url.

We've also done a calculation with the arguments and returned them.

#### Extra Ideas 

See if you can make other routes work, e.g. minus, divide, multiply.

### Step 4 - Adding HTML

These pages look really boring. We can update it with a bit of HTML.

We need a new folder called `templates` and in that folder we'll make a 
file called `html-add.html`. In that file write the following:

```html
<!DOCTYPE html>
<title>Show the Number</title>

<h1 style="color:red">You calculated a number!</h1>
<h2 style="font-family: Courier">You added these numbers together...</h2>
<h3><em>{{ num1 }}</em></h3>
<h3><strong>{{ num2 }}</strong></h3>
<h2 style="font-family: Courier">To make...</h2>
<h3>{{ result }}</h3>
```

This may look a little weird to others who have done html before. But we're
actually going t use a special "templating syntax" in Flask so it can do 
some things for us. The `{{ result }}` line for example, will be replaced by 
a variable we give called `result`.

To do this write the following function in you `calculator.py`:

```python
from flask import Flask, render_template

# Keep the rest of what you've done here.

@app.route('/add-html/<int:num1>/<int:num2>')
def add_html(num1, num2):
    return render_template('html-add.html', num1=num1, num2=num2, result=num1 + num2)
```

Now restart the ap and in your browser go to `localhost:5000/number-html/4`

You now have a slightly styled web page!

#### What have we done

Flask has a special function called `render_template`, this looked for a 
HTML template using the name we've given (`html-add.html`) and, using
variables we give (in this case `num1=num1, num2=num2, result=result`),
renders the template with the data we want.

By default it will look for the templates in a directory called `templates`.

Easy!

#### Extra ideas

Create your own template! If you understand HTML and CSS feel free to 
create your own styling and make it as adventurous as you want.

If you know JavaScript you can even add that in.

### Step 5 - POST requests

While using the URL is a common way of deciding where to go and what
to display - it is not the only way of doing this.

So far we have been using what you call `GET` requests - these are the 
default requests you send when you type into a browsers address bar.

Another very common type of request is the `POST` request. We're going 
to use this for our calculator.

This time do the following:

```python
from flask import Flask, request

# Keep the stuff you've already written above here.

@app.route('/add_post', methods=['POST'])
def add_post():
    return str(int(request.form['num1']) + int(request.form['num2']))
```

Rerun the application, but instead of going to the browser this time, 
open up IDLE or a python terminal and run the following:

```pythonstub
>>> import requests
>>> response = requests.post('http://localhost:5000/add_post', data={'num1': 1, 'num2': 2})
>>> response.content
b'3'
```

As we can't make POST requests right now in the browser, we have to use
a library like `requests` to do it for us. But as we can see, if we change 
the numbers in the data dictionary, the response content will change to match.

#### What have we done?

The main thing we've done is we've removed the arguments from the URL. 
Instead we've moved them into a `form` which sits inside the `request`.

The `request` is what we send a web server when we ask for a website.
Inside the `request` are lots of bits of information, some of this is
stored inside the `form` which is where a users data can go in the form 
of a dictionary. In this case our `dictionary keys` (or `form fields`)
are `num1` and `num2`. Both of which should be an `int`.

Sadly it's not easy to send a POST request to a website in a browser
without more work. So we have to test this first by using the `requests`
library which allows us to make `POST` requests to any website we want.

#### Extra ideas
 
- Try add more fields to the form and do more complex calculations.
- Add more routes for other operators e.g. minus, subtract, divide.

### Step 6 - Forms

Now we have made our POST route, it's time to make a form for it.

We need a new html template. Let's call it `calculate.html`. Don't
forget to put it in the templates folder.

```html
<!doctype html>

<title>My Calculator</title>

<form action="{{ url_for('add_post') }}" method="post">

    <label for="num1">Number 1</label>
    <input type="number" name="num1" id="num1" placeholder="num1" />
    <br>
    <label for="num2">Number 2</label>
    <input type="number" name="num2" id="num2" placeholder="num2"/>
    <br>
    <button type="submit">Submit</button>
    
</form>
```

Now create a function like so:
```python
@app.route('/calculate')
def calculate():
    return render_template('calculate.html')
```

Restart the app and go to `localhost:5000/calculate` in your browser and 
try it out!

#### What have we done?

We've created a form in HTML which will do `POST` requests for us. It will
send the form data to our `add_post` function which returns the correct number.

#### Extra ideas

If you created POST routes for other operators, e.g. subtract, divide etc. You
can use this same template for those routes. You just need to change the forms
action.

If you can think of how you could do all of these in a single route.