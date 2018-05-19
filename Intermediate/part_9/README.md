# Beginner Python - Part 9

Welcome to your tenth python lesson!

In this lesson we're going to learn to read and write to files
as well as how to encode and decode basic "secrets".

## Opening files in python

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

### File modes
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

### Binary modes

There are two main types of text in programming, Unicode and Bytes. 
Unicode is what we are used to reading on our screens, it includes the
alphabet, numbers, symbols and everything else up to and including
emojis.

Bytes on the other hand is what the machine _actually_ sees, which to
humans normally looks like nonsense. Luckily python has a special type of
string called a byte string which looks like normal text to us, but 
python translates for the machine.

If we want to use these byte strings we prepend our strings with a `b` like
so:

```python
b'This is a byte string'
```

Sometimes when reading and writing files we need to read them as byte strings
instead of unicode, in which case we have to open them in binary mode. We do this
by adding a `b` to our normal mode:

```python
read = open(filename, 'rb')  # a file in binary read mode.
write = open(filename, 'wb')  # a file in binary write mode.
```

## Secrets in Python

There are many ways of creating "secrets" in the programming world, they
generally fall into two categories:

1) Reversible secrets (encoding and encryption).
2) Irreversible secrets (hashing).

Encoded and encrypted secrets are for secrets you want people to eventually 
be able to read. We use them for things like secure websites, and will use 
them in this example.

Hashed secrets are for secrets you never want people to read, but you want
to check if people know - this is primarily for passwords.

## The Lesson

We are going to write two functions, one that reads a secret from a file 
and one that writes a secret to a file.

The function that reads the file will try to decode the contents using
the python `base64` encoding library. Whereas the one that writes to the 
file will encode the message using `base64`.

### Part 1 - import `base64`

You should know how to do this by now:

```python
import base64
```

This library has two functions we are going to use:

1) `base64.decodebytes()` - for decoding a secret.
2) `base64.encodebytes()` - for encoding a secret.

### Part 2 - Writing to a file with a function

We want a `write_secret` function which takes a filename and some
text as arguments. It should then open the file in binary write mode,
convert the text into bytes (using the `bytes` function) and write the
text to the file:

```python
def write_secret(filename, secret):
    encoded_secret = base64.encodebytes(bytes(secret))
    with open(filename, 'wb') as new_secret:
        new_secret.write(encoded_secret)
```

Try and run your code and write something to a file. Take a look to see
what it made.

### Part 3 - Reading from a file with a function

We want a `read_secret` function which takes a filename as an argument.
It should then open the file in binary read mode, read the lines and decode 
them:

```python
def read_secret(filename):
    with open(filename, 'rb') as secret:
        for line in secret:
            print(base64.decodebytes(line))
```

Try and run your file and read what you made in the last section. Does it
come out with the correct message?

## What have we done?

We've learnt how to read and write from files in different modes.

We've also learnt about secrets in programming and how to make our own.

Keep in mind, `base64` secrets are not very secure. But they're probably
good enough to stop most people understanding what you've written.

### Next

Try and see if there is anything else you can build with this. Like a
secret messaging system.

You can also play around with writing anything to file, for example 
you could ask people questions and store their answers - creating
a pseudo learning program.

If you want to do something really weird you can even write python files
using python (this is how IDLE works).