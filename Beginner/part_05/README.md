# Beginner Python - Part 5

Welcome to your sixth python lesson!

We're going to finish up by learning some about for loops and a 
new data type.

## The Lesson

### Lists

Lists are a very common data type in python which, as you 
may have guessed, hold a list of other data.

They look like this:

    [1, 2, 3, 4]

This is a list holding the integers 1 to 4. But lists can hold 
any form of data in any combination, for example:

    [5, 'Hi', 3.2, [1, 2, 3], print]

This is a list that is holding integers, strings, floats, another 
and the print function.

_N.B. if you hadn't realised already, functions are also 
a type of variable and can be stored like everything else._

The important thing about lists is that they hold *anything* and
that they keep them in the order you put them in. 

### For loops

We've done `while` loops, now we need to look at `for` loops.

`for` loops are different because they don't use a condition
to define when they stop. Instead they take a list of objects
and do something for every object in that list.

For example:

```python
for thing in [1, 2, 3]:
    print(thing)
1
2
3
```

In this example we simply made a list of numbers and printed all
of the numbers.

## The Exercise

We're going to be using turtle again, except this time instead of
calling out every function ourselves, we're going to make a list
of  turns we want to make and loop over it.

### Step 1 - Setup turtle

This bit is easy:

```python
import turtle

turtle.shape('turtle')
```

### Step 2 - Define the list

Now we need to save the list into a variable, this should be
fairly obvious by now.

```python
turns = [90, 90, 90, 90, -90, -90, -90, -90]
```

### Step 3 - Loop over the list

Let's write our for loop.

We named our list "turns" so we will loop over that:

```python
for turn in turns:
    turtle.forward(40)
    turtle.left(turn)
```

And that should be everything.

Your file should look like [this](turtle2.py).

## What have we done?

We've finished up our control flow lessons with a for loop and
we've found out what lists are.

We've found that for loops are really useful for doing the same
set of actions to a list of objects.

### Next

Play around with the list and make the turtle draw different shapes.
