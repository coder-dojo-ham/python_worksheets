# Beginner Python - Part 6

Welcome to your seventh python lesson!

We're going to finish up by learning how to make a function, as well
as learning how to use the `range` function.

## Making functions

We've used a lot of functions already - remember they're the things you
put brackets after like `print()`.

Now we'll learn how to make them.

Functions are made by using the `def` keyword, a name you choose and
then a list of arguments between a pair of brackets, and finally
some code. For example:

```python
def my_func(argument_1, argument_2):
    print(argument_1)
    print(argument_2)
```

It will then run everything indented after this line with those 
variables. However it will only run _after_ you call the name with 
brackets.

Whatever you put between the brackets will be put into the arguments you
made.

```python
>>> my_func('Hello', 'There')
Hello
There
```

## The range function

`range` is a function in Python which generates a list of numbers 
up to (but not including) a given number.

We can see this in action using a `for` loop like so:

```python
for num in range(10):
    print(num)
```

This will print numbers from 0 to 9.

As we can see `for` loops follow a pattern of `for new_var in var`.
It assumes `var` has several objects within itself. It then goes through 
each object and assigns it to `new_var`, then executes everything indented
after itself.

Now let's make something more interesting.

## The lesson

We're going to make a turtle which draws a shape for us based on a
number we give it.

So open a new file and get ready.

### Step 1 - import turtle and set the shape

This bit is easy:

```python
import turtle

turtle.shape('turtle')
```

### Step 2 - create the function

We're going to call the function `shape`.

It will take the number of angles we want the shape to have
and based on that figure out how much the turtle needs to turn.

We will then run a `for` loop to make the turtle draw and turn the 
right number of times.

#### Step 2a - naming the function

Add the following to the file:

```python
def shape(angles):
```

This gives us the function name and it's argument name, `shape`
and `angles`.

#### Step 2b - figuring out how much the turtle turns

We are working with degrees and all of a shapes angles need to add
up to 360. So we need to divide 360 by the number of angles we want.

Expand the function to look like this:

```python
def shape(angles):
    turn = 360/angles
```

#### Step 2c - drawing the shape

Now we have the number of angles and the amount the turtle turns
all we have left to do is draw it.

We will use a `for` loop which will execute for the number of
angles there are in the shape. We will use `range` to give the
for loop this number.

Expand the function to look like this:

```python
def shape(angles):
    turn = 360/angles

    for _ in range(angles):
        turtle.forward(50)
        turtle.left(turn)
```

That's the entire function!

Your file should look like [this](turtle3.py).

## Running the file

When you run the file nothing will happen.

This is because although you've defined your function you haven't 
used it yet.

Run the file and you should get an interactive prompt.

In the prompt run this:

    >>> shape(4)

The turtle should draw a square.

You can use it again and again with any number you want to keep
drawing.