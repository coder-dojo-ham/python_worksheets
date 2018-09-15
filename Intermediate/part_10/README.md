# Beginner Python - Part 10

Welcome to your eleventh python lesson!

In this lesson we're going to learn to read and write to files.

## The Lesson

### Opening files in python

Files are a core tool in python and essential to saving "state".

To use files we have to open and close them. The easiest way to do
this is with the `open` function and `.close` method like so:

```python
file = open('file.txt')  # I've opened the file.
file.close()  # Now I've closed it.
```

However this is an old method and can be dangerous, if you forget to
close the file, or the program has a bug, the file can become corrupt.

To solve this we have a special `with` keyword which makes sure we
_always_ close the file:

```python
with open('file.txt') as file:
    file.read()
```

#### File modes
We can also open files in different "modes". The default mode is read 
only, so we cannot write to the file but can read it's contents.

```python
with open('file.txt') as file:
    for line in file:
        print(line)  # prints every line of the file.
```

To write to a file we need to open in write mode which we do like so:

```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!')
```

Be careful when using write mode, if you open an old file in this mode
it will delete all the contents of it and treat it as a blank file. Even
if you don't actually write anything!

If you want to just write to the end of a file you should use the append mode
which can be done like so:

```python
with open('file.txt', 'a') as file:
    file.write('Hello, World again!')
```

This will open the file and add text to the end of it instead of overwriting 
the file.

### New lines

Weirdly writing on a newline requires a special character. If you don't
include the special character then everything gets written on the same line.

The special character is `\n`. Include it at the end of the text you want
to write a new line.

For the above it would look like:

```python
with open('file.txt', 'w') as file:
    file.write('Hello, World!\n')
```

## The Exercise

We're going to use the fizzbuzz function we made in the last lesson to read
a file full of numbers and replace them in a new file with fizz, buzz, fizzbuzz
or the same number.

### Step 1 - make a file full of numbers

You can do this by hand or using python. Each number should be on a new line.

Let's call the file `numbers.txt`. To make it with python we can import random
and create a given number of random numbers.

This should be done in a function so it only happens on demand.

The following should work just fine:

```python
import random


def generate_random_numbers():
    with open('numbers.txt', 'w') as file:
        for _ in range(100):
            file.write(str(random.randint(0, 1000)) + '\n')
```

In a python terminal import this function and run it to make the file of 
random numbers.

### Step 2 - import the fizzbuzz function

We will assume you have the file with the fizzbuzz function in the same folder as 
the file you are currently writing. We will also assume this file is called 
`fizzbuzz.py`. If this is the case you can import the function like so:

```python
from fizzbuzz import fizzbuzz
```

### Step 3 - write the function to fizzbuzz a file

We are going to create a function which opens two files, an input
and an output file. We'll allow the names of these files to be changed with
default arguments.

We'll open both files in a single `with` statement and start reading the input
file before running fizzbuzz on the file.

#### Step 3a - create the function and with statement

Lets start with the with statement:

```python
def fizzbuzz_file(input_name='numbers.txt', output_name='fizzbuzz.txt'):
    with open(input_name) as input_file, open(output_name, 'w') as output_file:
```

As you can see we have opened two files in a single with statement, separating
them with commas.

#### Step 3b - Start reading the input file

Let's start reading the input file now. As python assumes everything in a file
is made of text we'll have to manually convert the lines into integers.

```python
def fizzbuzz_file(input_name='numbers.txt', output_name='fizzbuzz.txt'):
    with open(input_name) as input_file, open(output_name, 'w') as output_file:
        for num in input_file:
            num = int(num)
```

#### Step 3c - fizzbuzz the file

Now we have the number as an integer we can check it for fizzbuzz.

We have to make sure the result is a string and then write it to the output
file. Don't forget to include the newline.

```python
def fizzbuzz_file(input_name='numbers.txt', output_name='fizzbuzz.txt'):
    with open(input_name) as input_file, open(output_name, 'w') as output_file:
        for num in input_file:
            num = int(num)
            result = str(fizzbuzz(num))
            output_file.write(result + '\n')
```

### Step 4 - add a main block

Finally lets add a main block to run the whole thing:

```python
if __name__ == '__main__':
    generate_random_numbers()
    fizzbuzz_file()
```

Finally run the file and we are finished.

## What have we done?

We've discovered how to read and write to files.

To explore this we imported a function we made previously and applied it
to a file of numbers - writing the output somewhere else.

### Next

Try playing with what you write to the output file. Maybe include the 
original number so you can check the result by hand.

You can play around with writing anything to files, for example 
you could ask people questions and store their answers - creating
a pseudo learning program.

If you want to do something really weird you can even write python files
using python (this is how IDLE works).