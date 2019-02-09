# Beginner Python - Part 6

Welcome to your seventh python lesson!

Here we're going to learn more about the `list` data type.

We will also introduce the `len` function.

## The Lesson

### What is a list

A list is an ordered collection of variables.

They are made with square brackets like so:

```python
a = [1, 2, 3, 4, 5]
```

### How can we use them?

We've already seen how we can use them in for loops, but we
can also access the data inside them by "slicing" and "indexing"
them.

#### Indexing a list

Indexing a list is when we want to access just one item in the list.

We do this by putting the "index" of the item we want to get in square 
brackets after the list variable. For example:

```python
a = [1, 2, 3, 4, 5]
b = a[0]  # b == 1
c = a[2]  # c == 3
d = a[1] + a[3]  # d == 6
```

In this example we define a list of integers from 1 to 5, we then
take the first item in this list (1) and assign it to the variable `b`.
We assign the third item (3) to `c`. Finally we assign the sum of the 
second (2) and fourth (4) item to `d`. 

It may sound strange that we get the first item using `[0]`, this is
because (as pointed out in the first lesson) python starts counting from 0.
Python is what you call a 0-based language.

#### Slicing a list

Slicing a list is when you want to get multiple items from the list
at the same time.

Where indexing returns a single item, slicing will return a list
with the requested items in it.

Again we use square brackets to define what we want, but we use
two numbers separated by a colon to denote the beginning and end of
the section we want.

```python
a = [1, 2, 3, 4, 5]
b = a[0:2]  # b == [1, 2]
c = a[2:5]  # c == [3, 4, 5]
d = a[2:100]  # d == [3, 4, 5]
e = a[2:2]  # e == []
```

Slicing strangely lets you put in any combination of numbers, even 
if it exceeds the number of items there are - if you go beyond the
lists limit it will just ignore it. 

### The `len` function

The `len` function simply returns the length of an object.

This works for strings, lists and anything else which may have a length.

```python
a = len([1, 2, 3, 4, 5])  # a == 5
b = len('How long is a piece of string?')  # b == 30

```


## The Exercise

Now we know different ways of using a list we're going to have a bit
of fun with them and make a random food generator.

### Step 1 - import random

We'll need to import `random` to make a random food generator.

Lets do that:

```python
import random
```

### Step 2 - define some random food lists

Lets make two lists, one for food and another for toppings:

```python
food = ['Macaroni', 'Chicken', 'Spaghetti', 'Fish', 'Eggs', 'Sausage', 'Noodles', 'Omelette', 'Mushrooms', 'Caramel', 'Chocolate']

toppings = ['Cheese', 'Rice', 'Meatballs', 'Chips', 'Toast', 'Mash', 'Salad', 'Ice Cream', 'Quiche', 'Milk']
```

You can replace these with anything you want.

### Step 3 - make a random meal

Now we can use `random` to generate a random index from the
length of the list.

We can index the list with this to get our random foods which we print out:

```python
random_food = food[random.randint(0, len(food)-1)]

random_topping = toppings[random.randint(0, len(toppings)-1)]

print('For today dinner is ' + random_food + ' and ' + random_topping + '!')
```

#### N.B. We could just use `random.choice` instead of indexing as well.

## What have we done?

We've learnt more about what lists are and how we can use them.

Specifically we learnt about slicing and indexing.

We also learnt about the `len` function.

## Next

Play around with the lists, maybe make a generator for something 
other than food.