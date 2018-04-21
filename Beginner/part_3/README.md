# Beginner Python - Part 3

Welcome to your fourth python lesson!

We're learning about "control flow" in this lesson.

## What is control flow?

Control flow is how we control what a program can and can't do.

The 2 main ways to do this are:

- If statements - We use these to check if something is true 
  and to do something if it is (or isn't).
- Loops - these allow us to do the same thing over and over again
  as many times as we need.

We will focus on if statements in this lesson.

## If statements

If statements are a special way to do something only if something 
else is "true".

We write them like this:

```python
years = int(input('How old are you ' + name  + '? '))

if years > 10:
    print('You are older than 10.')
else:
    print('You are 10 or younger.')
```

The `if years > 0:` checks to see if `years` is greater than 0. If it is 
python will run everything indented after that line.

If it isn't true python will execute everything indented after the
`else:` line.

You can also use `elif` statements to check extra possibilities like so:

```python
if years > 10:
    print('You are older than 10.')
elif years < 5:
    print('You are younger than 5.')
else:
    print('You are between 10 and 5.')
```

## The lesson

### Step 1 - getting the age

We are going to largely copy what we did before aside from the last
task:

```python
name = input('What is your name? ')

print('Hi ' + name + ' I am Python!')

years = int(input('How old are you ' + name + '? '))

months = years * 12
```

### Step 2 - making the if statement

Now all we hae to do is write a statement to check how old
the user is and react accordingly.

Here is an example:

```python
if years > 18:
    print(name + ' did you know that you are ' + str(months) + ' months old? That is pretty old!')
elif years < 4:
    print(name + ' did you know that you are ' + str(months) + ' months old? That makes you a baby!')
else:
    print(name + ' did you know that you are ' + str(months) + ' months old?')
```

Feel free to change the ages used and the text to write something else.

That's it!