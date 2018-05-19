# Beginner Python - Part 0

Welcome to your first Python lesson!

In this task we're going to write our first Python program.

But first we should cover some absolute basics.

## The Lesson

### Variables and Types

#### Variables

Python uses "variables" to store information, if you've worked
with Scratch you may already be familiar with this.

Variables are just names we give to pieces of data we want to use.

For example put this into your console:

    >>> my_var = 1
    >>> my_var
    1

You just created a variable called "my_var" and gave it a value of 
`1`.

Try making another variable with another name.

#### Types

Different variables have different "types" in Python. The one we
made above has a type of `Int`, which is short for integer, which
 means a whole number.
 
There are a few other types, the ones we care about the most are:

- `Int` - for whole numbers.
- `Str` - for text (`Str` is short for string).
- `Float` - for decimal numbers.

These are defined in different ways.

Integers are defined by giving a variable a number:

    >>> my_int = 1

Strings are define by wrapping something in either single or double
quotation marks like so:

    >>> my_str_1 = 'Hello'
    >>> my_str_2 = "Hello again"

Floats are define by using a decimal point:

    >>> my_float = 1.5

#### Using variables together

Variables can be used together with "operations". These include
things like adding and subtracting.

Try adding two integers together. You should have something like:

    >>> 1 + 2
    3

Or adding two strings:

    >>> "Hello" + "there"
    'Hellothere'

But one thing we cannot do is mix types:

    >>> "Hello" + 1
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: must be str, not int
    >>> 1 + "2"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    

This gives us an error telling us what went wrong.

### Functions

Functions are a core part of any programming language. They are
a way for you to write code once and then use it over and over
again. Kind of like copy and pasting, but much faster!

We aren't going to make functions just yet, but we will use them.

We know something is a function when we put brackets at the end 
of a variable name like this:

    >>> print()

When we do this it means we are "calling" a function and telling 
it to do something.

Python has lots of functions already ready for you to use.

The `print` function is a function which can show us data on the 
screen.

To do this we need to pass it an "argument", this is something we
put in between the brackets, like a variable.

#### Capturing the output of functions

Some functions "return" and output. This means they create something
new which you can put into a variable.

For example the `str` function turns a variable into a string:

    >>> str(1)
    '1'

We can put this into a variable like so:

    >>> my_one = str(1)
    >>> my_one
    '1'

### Comments

Comments are how we explain what is happening in our code.

We write comments by using a `#`. anything after a `#` is a comment
and Python will ignore it when running.

For example:

    >>> print(1)  # This is a comment
    1

#### Using functions to change types

Another set of useful functions that Python gives us are functions 
change the type of an object.

Here is a list of the ones we might use:

- `int` - Tries to change a variable into a whole number.
- `str` - Tries to change a variable into text.
- `float` - Tries to change a variable into a decimal number.

We can use these to fix the errors we had earlier:

    >>> "Hello" + str(1)
    'Hello1'
    >>> 1 + int("2")
    3

### Our first program.

We can keep writing code in our interactive prompt (the thing which
starts with `>>> `) but then we'll lose everything when we close the
window.

To save our Python programs we need to put them in python files 
which end with a `.py`. 

Take a look at the file [hello.py](hello.py), this is what we are
going to do first.

We are using the `print` function, and passing it an "argument" of
"Hello, World!".

Open a new file in IDLE and write the code into there. Save it and then run 
the file.

You should see "Hello, World!" in your console.

## Why are we starting from 0?

Normally you would start from 1, but in many programming languages,
including Python, they start counting from 0. This will be explained
more later.
