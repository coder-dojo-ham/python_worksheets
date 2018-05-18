# Beginner Python - Part 5

Welcome to your sixth python lesson!

We're going to finish up by learning some about for loops and a 
new data type.

## Lists

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

## For loops

We've done `while` loops, now we need to look at `for` loops.

`for` loops are a different because they don't use a condition
to define when they stop. Instead they take a list of objects
and do something for every object in that list.

For example:

```python
>>> for thing in [1, 2, 3]:
        print(thing)
1
2
3
```

In this example we simply made a list of numbers and printed all
of the numbers.

## The Lesson

We're going to be using turtle again, except this time instead of
calling out every function ourselves, we're going to make a list
of turns we want to make and loop over it.
