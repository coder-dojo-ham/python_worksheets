# Beginner Python - Part 2

Welcome to your third python lesson!

We're learning a new and very useful function in this lesson:

`input`

## The Lesson

### What is `input`?

`input` is a special function which allows you to ask the user for
input. You can ask people questions!

It takes one argument which is the question you want to ask.

Always end the question with a space after the question mark
 otherwise it looks a bit weird.

#### Try it out

In an interactive prompt, put in the following:

    >>> input('What is your name? ')

You'll see the question printed below and it will let you type next
to it. When you hit enter it will print what you wrote on the 
screen.

#### Catch the output

In the same way we catch output from other functions we can capture
the output from `input`. Like so:

    >>> name = input('What is your name? ')

Now if you print `name` it will tell you what the user wrote.

#### A warning

`input` will _always_ return a string. So if you want a number you'll
have to use `int` to convert it.

## The Exercise

Now let's do the task.

In this lesson we are going to ask a user for their age.

Once we have their age we're going to tell them (roughly) how old
they are in months.

Open a new file.

### Step 1 - get their name

As we did earlier let's take the users name first.

Add this to the top of the file:

```python
name = input('What is your name? ')

print('Hi ' + name + ' I am Python!')
```

If you run this now it will ask you for your name and then say hi.

Feel free to change any of the text to say what you want it to say.

### Step 2 - get their age

This bit is a bit complicated, we're passing the output of a function
directly into another function. It may sound weird but it's no
different than putting a variable in as an argument.

Add this to your file:

```python
years = int(input('How old are you ' + name + '? '))
``` 

We want the persons name to be a number so we convert the output of 
`input` immediately into a number and put this in the variable `years`.

### Step 3 - telling the user their age in months

For the final step we multiply years by 12 to get the number of months
and print the result.

Remember we need to convert the number back into a string to add the 
text together.

Here are the last two lines:

```python
months = years * 12

print(name + ' did you know that you are ' + str(months) + ' months old?')
```

You can see the full code [here](age1.py).

## What have we done?

In this lesson we've learnt about the `input` function - an extremely
useful function for making our programs work for everyone.

### Next

Play around with this function and see if you can make anything else 
interesting with it.
