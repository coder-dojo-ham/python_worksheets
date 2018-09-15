# Turtle racer

In this project we're going to create Turtle objects which
can race each other.

This will teach us Object Oriented Programming. 

## Getting Started
### What you need to know already

To do this project you need to understand:

- Variables.
- If statements.
- Functions.
- Object basics

### What we are introducing in this project

This project focuses on teaching you about:

- More about objects.

## The Project

### Step 1 - The Class

Create a file called `turtle_racer.py` and write the following in it:

```python
import random
import turtle


class TurtleRacer(turtle.Turtle):
    pass
```

#### What have we done?

We've created a `class` called `TurtleRacer`. A class is like a common _type_
of _object_. If an object is of a type `String` it will have all the properties
of a `String`. If the object is of a type `TurtleRacer` it will have all the properties
of a `TurtleRacer`.

One of the cool things about classes is something called _inheritance_. This means
we can take all the properties from one class and put them into another. We can then
use those properties as they are, or edit them to do something else.

In this case we have made a class called `TurtleRacer` and hae made it inherit from
the `turtle.Turtle` class by putting `turtle.Turtle` inbetween brackets before the colon.

This means our `TurtleRacer` can behave exactly as you'd expect a python `Turtle` to behave.

### Step 2 - Adding some basic properties to the TurtleRacer

Edit our `TurtleRacer` object to look like this:

```python

class TurtleRacer(turtle.Turtle):
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.shape('turtle')
```

#### What have we done?

We've added a special _method_ to our class. A _method_ is just a fancy name for a 
function that sits inside (is indented inside) a class. They always have at least 
one argument called `self` which refers to the object we are using. By using `self`
in our methods we can alter the object.

`__init__` itself is a special method which is called when we create a new object of 
our class type. Or we `initialise` an object. This is the method which sets up most
of the special properties our object will have.

Aside from `self` we have three more arguments. `name` which is what we will call
the `TurtleRacer`, and `*args` and `**kwargs`. `*args` and `**kwargs` are lazy ways
of saying "I don't know how many argument we will get so I'll just accept everything".

We then call the `super` method and pass it all the unknown arguments we could get.
This finds the same `__init__` method on the class `TurtleRacer` inherits and runs
it - making sure we get all the properties we want.

Next we set the turtle name by taking the argument `name` and setting it to 
`self.name`. Finally we run `self.shape('turtle')`. This ensure our turtle
actually looks like a turtle.

### Step 3 - Get Ready!

Now we have started building our class - we need our turtles to find their
starting position. Lets make a new method to do that. Don't delete any of the code
you've written so far - simply add the following to your class. I've put in a comment
like so `#...` to mark where old code should be kept.

```python
class TurtleRacer(turtle.Turtle):
    #... Keep the __init__ method here.

    def starting_positions(self, y):
        self.penup()
        self.setx(-turtle.window_width()/2)
        self.sety(y)
        self.pendown()
```

#### What have we done?

We've created a new method, `starting_positions`, which set's the x and y coordinates
of the turtle. The x coordinate is always the same place - so all turtles start at
the starting line. But the y coordinates differ so turtles can be above or below
eac other.

The x coordinates are set to the negative width of the window divided by 2. This is 
because the centre of the window is the x coordinate 0. So the negative half width of
window is the left most edge.

`penup` and `pendown` ensures we don't draw on the screen when starting the turtles.

### Step 4 - Get Set!

Now we can setup the turtles on a starting line we should actually create some 
`TurtleRacer` objects.

Add the following code below your class:
```python
screen = turtle.Screen()

turtle1 = TurtleRacer('Donatello')
turtle2 = TurtleRacer('Leonardo')
turtle3 = TurtleRacer('Raphaelo')

turtle1.starting_positions(-100)
turtle2.starting_positions(0)
turtle3.starting_positions(100)

screen.turtles = [turtle1, turtle2, turtle3]

finished = False
```

#### What have we done?

We have created a screen to put the turtles on. We create an object of the class
`turtle.Screen`. We then follow this up by making 3 `TurtleRacer` objects. I've named
them after TMNT but you can call them whatever you want.

After we create the racers we set their starting positions. One is at y coordinates -100,
another at y coordinate 0 and a last one at y coordinate 100.

We put all our turtles in a list and attach the list to the screen as `screen.turtles`.
This doesn't do anything actively - but it puts all the turtles in place so we can access 
them easily.

Lastly we set a Boolean variable called "finished" to `False`. We're going to use
this variable to tell us if the race finishes.

### Step 5 - GO!

Lets add in the race logic so our turtles can actually race!

Below the code you just put in add the following:

```python
while not finished:

    for turtle_racer in screen.turtles:

        turtle_racer.forward(random.randint(1,10))

        if turtle_racer.xcor() >= turtle.window_width() // 2:

            turtle_racer.home()
            turtle_racer.write(turtle_racer.name + ' won!', font=('arial', 24, 'bold'))
            finished = True
            break

turtle.exitonclick()
```

#### What have we done?

This is our racing logic.

We start a while loop which will keep running as long as we are `not finished` or 
as long as finished is `False`.

In this while loop we also have a for loop which loops through `screen.turtles` this
is the list of our `TurtleRacers` we made earlier. It goes through every turtle and
tells it to move `forward` by a random number between 1 and 10.

We then have an if statement, `if turtle_racer.xcor() >= turtle.window_width() // 2:`

This if statement checks a turtle racers x coordinates and sees if it is far enough across 
the screen - we define this as half the window width. As with above where the negative half
window width is the left edge. The positive half window width is the right edge.

If the turtle has reacher or gone beyond this destination we send the turtle `home` and make
it write on the screen that it won. We set `finished` to `True` and `break` the for loop.

This ends both the for and while loop.

`turtle.exitonclick()` keeps the window from immediately closing.

That's it! You've made racing turtles.

### Extra

See if you can add extra methods to your turtle.

I make my turtle do a 360 when it wins. I do this by adding a 360 method to my turtle
like below:

```python
class TurtleRacer(turtle.Turtle):
    #... Keep all the __init__ and starting_positions logic you did earlier.
    
    def do_a_360(self):
        self.left(360)
```

And then adding the following code in the while loops if statement, I added it just after
 the `turtle_racer.home()` command:

```python
while not finished:

    for turtle_racer in screen.turtles:

        turtle_racer.forward(random.randint(1,10))

        if turtle_racer.xcor() >= turtle.window_width() // 2:

            turtle_racer.home()
            turtle_racer.do_a_360()
            turtle_racer.write(turtle_racer.name + ' won!', font=('arial', 24, 'bold'))
            finished = True
            break

turtle.exitonclick()
```

What else can you add?
