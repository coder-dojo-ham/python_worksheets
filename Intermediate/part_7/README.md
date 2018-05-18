# Beginner Python - Part 7

Welcome to your eighth python lesson!

We're going to learn about a new library, the `datetime` library.
Once we understand what it is for we are going to use it to `refactor`
some of our old code.

## What is the `datetime` library?

In python the `datetime` library is what we use for handling dates and times.

You may remember in part 2 we tried to work out how old
people are in months, but it wasn't very accurate. With the `datetime` 
library we can work out how old someone is to the day, if we have the exact
time they were born we could tell them how old they are in seconds.

There are three new types this library introduces that we care about:

1) `datetime` - this is a type which holds both a date and a time.
e.g. 4PM on the 12th of May 2018.
2) `date` - a type which holds just a date. e.g. the 12th of May 2018.
3) `timedelta` - a type which holds a length of time. e.g. 4 days.

## What is refactoring?

Refactoring is the practice of improving code over time.

Programmers rarely write perfect code the first time. Sometimes they didn't
know they could use a better tool, or they were in a rush and forgot about a
better way of doing things.

As a result it is very common to come back to old code and to improve it.
This is called refactoring.

Today we are going to refactor our original age calculating program from part 2
by making it much more accurate with the `datetime` library. 

## The lesson

We are going to ask for someones full date of birth and tell them
how old they are in days.

### Part 1 - import datetime

First things first lets import `datetime`:

```python
import datetime
```

### Part 2 - Asking a user for their date of birth

Whilst last time we only asked for their age, this time we need their
date of birth:

```python
year = input('What year were you born in: ')

month = input('What month number were you born on: ')

day = input('What day were you born on: ')
```

### Part 3 - Constructing the date of birth

Having just the numbers isn't enough, we need to create a `date` object
which holds the date of birth:

```python
dob = datetime.date(int(year), int(month), int(day))
```

### Part 4 - Finding the number of days they've been alive for

Now we have a `date` object we need to create a `timedelta` object which
holds the number of days they've been alive for.

We can create this by subtracting their date of birth from todays date:

```python
days = datetime.date.today() - dob
```

### Part 5 - Printing their age in days

This part is the easiest - just print the number of days with a message: 

```python
print('Did you know that you are ' + str(days.days) + ' days old?')
```

## What have we done?

We've learnt about the `datetime` library. Having figured out what it can do
we've refactored our age program from part 2.

We can now tell someone how old they are, accurately, in days.

### Next

Why not try to figure out how old someone is in minutes or seconds?

Or you could try and find out what is the age difference between two
friends.