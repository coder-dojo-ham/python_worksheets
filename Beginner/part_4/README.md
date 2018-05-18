# Beginner Python - Part 4

Welcome to your fifth python lesson!

We're learning more about "control flow" in this lesson.

## Loops

In the last lesson we mentioned loops, in this lesson we will use one.

There are two types of loops:

1) `for` loops.
2) `while` loops.

In this lesson we are using a `while` loop.

### What is a `while` loop?

A `while` loop is a loop which keeps doing the same thing over and over
until a condition is not met.

For example:

```python
num = 1
while num < 10:
    print(num)
    num = num + 1
```

This creates a variable called `num`. It then creates a `while` loop
which checks to see if `num` is smaller then 10. If it is it will 
execute everything indented after the `while` statement.

Here we print `num` and then increase it by 1. Eventually `num` will 
be 10 or greater, at this point the `while` loop will break and the 
program will end.

### Why are while loops useful?

While loops are part of something programmers call *DRY*, which
means *D*on't *R*epeat *Y*ourself.

In general when we code we try to never type the same thing twice.
Instead we use loops and functions to store the code once and then
do it multiple times.

The next few lessons are dedicated to tools we use to do this.

## The lesson

We are going to randomly generate a number and ask a user to guess it.

We will use a `while` loop to keep asking them until they get the number 
right and we'll use an `if` statement to give them a hint to get closer.

Let's open a new file and get started.

### Part 1 - generate a random number.

We need to import the `random` library and get a random number.

Put this at the top of the file:

```python
import random

target = random.randint(1, 1000)
```

This will give us a variable `target` which holds a random number 
between 1 and 1000. You can change this to any set of numbers you want.

### Part 2 - ask the user for a guess

Like we did when getting the users age, lets ask them to guess a number.

Add the following to the file:

```python
guess = int(input('Guess a number between 1 and 1000: '))
```

We are now storing the guess in a variable called `guess`

### Part 3 - write the loop

Now we need to write the loop.

We are going to keep going until `guess` is equal to `target`. This means
while `guess` is not equal to `target` we should stay in the loop.

We use `!=` to test if something is not equal (`==` is what we use to
test if something _is_ equal).

When in the loop we will check to see if `guess` is bigger or smaller
than `target` and let the user know.

Once they guess correctly we exit the loop and `print` another message

Add the following to your file:

```python
while guess != target:
    if guess < target:
        guess = int(input('That is too low! Try again: '))
    elif guess > target:
        guess = int(input('That is too high! Try again: '))

print('Yes! That is the number!')

```

## What have we done?

We continued learning about control flow in this lesson and found out
what a While loop is.

While loops are really good for doing the same thing over and over again.

### Next

You could try and make other guessing games, or perhaps make a turtle
constantly move around based on your input
