# Beginner Python - Part 1

Welcome to your second python lesson!

In this one we are going to `import` a library and use
it's functions.

## The Lesson

### What is importing?

Python has a _lot_ of functions you can use, but it likes to
hide them so programs don't get too big.

It does this by putting them in `modules` which you can `import`
to use the functions inside them.

A list of useful `modules` you may want to use are:

- `random` - for functions that produce random things.
- `math` - for functions which do math.
- `os` - for functions that work with your computer.
- `turtle` - for functions that draw on your screen.

To import a library you can either:

- Use just the `import` keyword like `import random`.
  This means to use the functions in the module you have to 
  always add `random.` in front. E.g. `random.randint(0, 10)`.
  
- Import a specific function from the module like 
  `from random import randint`. This means you can use the function
  directly like `randint(0, 10)`.
  
- Import _all_ the functions from the module in one go like
  `from random import *` (`*` means everything). You can use 
  the functions the same as above, but you might have a lot of 
  things you don't need and it may cause bugs.

## The Exercise

In this lesson we will import everything from turtle and use 
a few functions to draw on our screen.

Open a new file and call it something (not `turtle.py`).

At the top of your file put:

```python
from turtle import *

shape('turtle')

forward(50)

left(90)
```

Save it and run it. You should see a turtle appear on a screen.

It will move forward a bit, and then turn left.

## What have we done?

We've used a function from `turtle`, `shape`, to create a turtle 
image.

We then used the function `forward` to move it forward by 50 pixels
(50 is the number we gave it as an argument).

Finally we used the function `left` to turn the turtle 90 degrees.

Another set of functions we can now use are:

- `right` - to turn the turtle to the right.
- `back` - to make the turtle go backwards.
- `home` - to go back to where we started.
- `penup` - to stop the turtle drawing (it can still move though).
- `pendown` - to make the turtle draw again.

### Next

Have a play, let the turtle draw something on your screen. Get used 
to calling functions in Python.