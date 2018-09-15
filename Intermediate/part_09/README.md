# Beginner Python - Part 9

Welcome to your tenth python lesson!

We're going to carry on with functions in this lesson while
introducing three new concepts:

1) The main block.
2) The Modulus operator.
3) Default arguments in functions.

## The Lesson

### The main block

The most important thing about functions is that we can reuse them.

This includes using them in other files and programs we write. We
do this by importing our own code. When you import a file it runs all 
the code within it. This means any functions you've written (and 
classes which we cover later) are created and made ready for use.
However any top level code outside of these will be run as is, often 
this isn't desirable.

This will make a function but won't run or print anything out when 
imported:

```python
def sum(a, b):
    print(a + b)
```

This will run and print when imported:

```python
print(1 + 2)
```

To make sure we don't run top level code on import we have to use 
something called a `main` block.

`main` blocks make sure the code inside them are only executed
when the file they are in is run directly run, not imported. So
the code will not run when the file is imported. They are generally 
found at the end of a file and in our case would look like:

```python
if __name__ == '__main__':
    print(1 + 2)
```

The key bit here that makes it a `main` block is the line:

```python
if __name__ == '__main__':
```

It is usually advised that any top level code that you don't want
to run when importing a file should be put inside one of these blocks.

### The Modulus operator

The [Modulus](https://en.wikipedia.org/wiki/Modulo_operation) is a 
mathematical operator that finds the remainder after division of two
numbers.

In python (and several other languages) the modulus is represented 
by the `%` sign.

Some examples:

```python
>>> 10 % 3
1
>>> 5 % 3
2
>>> 1000 % 300
100
>>> 10 % 2
0
```

### Default arguments

Usually when you write a function you include arguments. However sometimes
you'll expect to normally use the same arguments over and over again. To
deal with this, so we don't have to write out the same arguments again and
again, we can use something called default arguments. These look the same
as normal arguments but include a value with a name.

They look like this:

```python
def func(a, b=1, c=2):
    return a + b + c

print(func(1, 2, 3))  # prints 6
print(func(1))  # prints 4
print(func(1, c=8))  # prints 10

```

In this case `a` is a normal (or `positional`) argument, whereas `b` and `c`
are `keyword` arguments with defaults of 1 and 2. As you can see from the 
example, you can use all arguments, just the positional arguments, or any
combination in between.

The most important point is that you must _always_ fill positional arguments
whereas keyword or default arguments are optional.

## The Exercise

We're going to implement a game called FizzBuzz.

This is a simple game where you choose two numbers (normally 3 and 5) and then
count upwards. For every number that divides by the first chosen number 
(normally 3) instead of saying the number you say "Fizz". For every number that 
divides by the second chosen number (normally 5) you say "Buzz". And for
every number that divides by both you say "FizzBuzz".

We'll make a `function` which does this and then run it inside a `main` block.

### Step 1a - create the function

We'll make a function called `FizzBuzz` which takes 3 arguments.

The first argument is the number we're checking, the second is our `fizz`
number and the third will be the `buzz` number. We'll make these default 
arguments using 3 and 5 respectively.

It should start looking like this:

```python
def fizzbuzz(num, fizz=3, buzz=5):
```

### Step 1b - add the function body

Now we have our `def` line we need to add the function body to check the
numbers.

We need to ask if `num` divides by either `fizz`, `buzz` or both. We can
do this with the modulus or `%` operator. Remember this tells us the 
remainder after dividing two numbers together. If we want to find out
if a number divides by another pefectly then the modulus should return 0.

Use `if` statements to check what the number divides by. It should look roughly
like:

```python
def fizzbuzz(num, fizz=3, buzz=5):
    if num % fizz == 0 and num % buzz == 0:
        return 'FizzBuzz'
    elif num % fizz == 0:
        return 'Fizz'
    elif num % buzz == 0:
        return 'Buzz'
    else:
        return num
```

### Step 2 - add a main block

Now we have our function we can run the code and use the function directly.

However it would be nice to run the code in one go. Let's add a `main` block
so we can do this.

Choose a number you want to count to (I'm choosing 50). Make a `main` block and
in that block write a loop which uses the `fizzbuzz` function to count to that 
number.

```python
if __name__ == '__main__':
    for x in range(50):
        print(fizzbuzz(x))
```

That's it. Your file should look something like [this](fizzbuzz.py).

## What have we done?

We've created a function which calculates if a number is divisible by fizz or 
buzz using a new operator, the modulus.

We've discovered default/keyword arguments and used them to choose sensible
default fizz and buzz numbers.

We've also learnt about the `main` block and have used that to be able to run
code directly when we want, but avoid running it on import.

## Next

Can you create a main block which uses different numbers for fizz and buzz?

What happens if you change the order of the if statements?
    §