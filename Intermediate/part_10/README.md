# Beginner Python - Part 10

Welcome to your eleventh python lesson!

We're learning a very important concept in this lesson, 
Objects and Classes. We will also touch on GUIs.

## The Lesson

### What are objects?

Everything in Python is an object. An object is simply something
that has:

1) Properties - variables attached to an object.
2) Methods - functions attached to an object.

They are very useful for holding state

#### N.B. state is what a program, or part of a program, looks like at any given time.

### What are classes?

Classes are like templates for objects. We use them to define
what an object should look like, and then make objects from them.

Let's make a basic class and call it "Animal". We will give it an alive
property of `True` and a `die` method:

```python
class Animal:
    alive = True
    
    def die(self):
        self.alive = False

``` 

We can see here that while functions normally start with a `def` statement,
classes start with a `class` statement. Classes also don't require brackets
in their definition (although you can use them).

Defining a class property is as simple as putting a variable in the class.

Methods on the other hand are a bit more complex. They look like normal 
functions however they have to have at least one argument, `self`, which 
refers to the object you'll make with the class. 

#### Making objects from classes

Let's try out our class and make some objects, run your code in an interactive
prompt and do the following:

```python
>>> first = Animal()
>>> second = Animal()
>>> first.alive
True
>>> second.alive
True
>>> first.die()
>>> first.alive
False
>>> second.alive
True
```

Here we made two _objects_ using our `Animal` _class_, called `first` and 
`second`. And whilst they both have the same properties, based on the class,
when one dies it does not affect the others.

#### Class inheritance

Using classes as templates is one part of their usability. Another very
useful aspect is called _inheritance_. This is where a class can inherit
the template of another class, and then expand it. We do this by putting
the class we want to inherit in brackets when defining the new class.

Add this after your `Animal` class:

```python
class Mammal(Animal):
    legs = 4
    eyes = 2

    def speak(self):
        print('squeak')
```

Here we can see a new class, `Mammal`, inheriting `Animal` inside 
parentheses.

We add 2 new properties, legs and eyes, as well as a speak method.

Let's try it out:

```python
>>> first = Mammal()
>>> second = Mammal()
>>> first.legs
4
>>> first.alive
True
>>> first.speak()
squeak
>>> first.legs = 6
>>> first.legs
6
>>> second.legs
4
```

We can see that our first and second objects are again based on the same 
template, but can be changed separately.

We can also see that we can still access the properties and methods we 
inherited from `Animal` as well.

Let's take this even further and make another new class and inherit
`Mammal`:

```python
class Dog(Mammal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('My name is {}'.format(self.name))
```

Here we have made a `Dog` class which inherits from `Mammal`. But 
we aren't defining any new properties. Instead we are overriding the
`speak` to tell us the dogs name.

We have also created a special method called `__init__`. This method is
special because it is called as soon as we make an object. Python looks
for it and uses it without us having to do it ourselves.

We give the `__init__` method it's arguments when we start (or "initiate")
our object.

Let's try it out:

```python
>>> good_boy = Dog('Rex')
>>> good_boy.alive
True
>>> good_boy.legs
4
>>> good_boy.name
'Rex'
>>> good_boy.speak()
My name is Rex
```

We can see here that we've completely overwritten the `speak` method
and that the name we gave when making the object was passed into the 
`__init__` method.

## The exercise

Let's take what we've learnt and do something even more useful.

Classes and objects can seem weird at first but they are some of
the most powerful tools in python. And that is because we can take
someone else's code and use it ourselves without having to do any work.

We're going to inherit some code from a new library called `tkinter`.

By inheriting code from this library we will be able to make a simple GUI.

### Part 1 - import `tkinter`

Start a file with:

```python
import tkinter
```

### Part 2 - create the Button class

We're going to define a class called `TheButton` which inherits `tkinter.Tk`.

```python
class TheButton(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

You can see we've also defined an `__init__` method which takes
`*args` and `**kwargs` as its arguments. This is a cheat way of
copying the inherited `__init__` method so that when we overwrite it
we don't lose the original method.

### Part 3 - Add a button and command

Now we have the base for our GUI we need to add a "widget" - which will
be our button.

Adapt the code to look like this:

```python
class TheButton(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.the_button = tkinter.Button(self, text='Push the Button', command=self.button_press)
        self.the_button.pack()
    
    def button_press(self):
        print('You pushed the button!')
```

Here we have added a `the_button` attribute to the object when it is made.
This button will have the text 'Push the button' and when clicked will
call the method `button_press`.

### Part 4 - Starting the GUI

Add the following to the end of the file:

```python
the_button = TheButton()
tkinter.mainloop()
```

This creates an object, or instance, of `TheButton` class. The last line
sets up the "loop" which the GUI will run in so the window doesn't close.

Run the program and you should hae a button appear on screen which you 
can click.

Your code should look like [this](the_button.py).


## What have we done?

We've learnt about objects and classes - a very significant, and lengthy,
lesson.

We've learnt about inheritance and how we can use it. And we've used
inheritance to make a GUI in 10 lines of code.

### Next

What else could we do with objects?

Could we inherit anything else? or could we make an either bigger GUI? 