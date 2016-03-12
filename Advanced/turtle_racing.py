"""
This is a turtle racing program.

It will teach you a bit of advanced stuff about objects.

In it we are going to create a new type of turtle, one that can race.

We will pit three of them against each other to see who will be the winner.
"""

import turtle
import random


class TurtleRacer(turtle.Turtle):
    """
    This is the turtle racer class. It inherits from the Turtle class so we get all
    the same attributes.
    """

    def __init__(self, name, *args, **kwargs):
        """
        Most classes need this to add some default attributes.
        """
        super(TurtleRacer, self).__init__(*args, **kwargs)
        self.name = name
        self.shape('turtle')

    def starting_positions(self, y):
        """
        Lets get the turtles in their starting positions!
        """
        self.penup()
        self.setx(-turtle.window_width()/2)
        self.sety(y)
        self.pendown()

    def speak(self):
        print("Hi my name is " + self.name)

    def do_a_360(self):
        self.left(360)

    def do_a_180(self):
        self.right(180)

    def make_a_shape(self, angles):
        """
        Draw a shape with the given number of angles.
        """
        turn = 360/angles

        for _ in range(angles):
            self.forward(50)
            self.left(turn)


screen = turtle.Screen()

# Make the racers and give them names.
turtle1 = TurtleRacer('Donatello')
turtle2 = TurtleRacer('Leonardo')
turtle3 = TurtleRacer('Raphaelo')

# Lets set the starting positions so they don't collide.
turtle1.starting_positions(-100)
turtle2.starting_positions(0)
turtle3.starting_positions(100)

# We can store extra stuff in objects. Lets put the turtles here so we can loop through them.
screen.turtles = [turtle1, turtle2, turtle3]

# We need this to tell us if the race finished
finished = False


while not finished:

    for turtle_racer in screen.turtles:

        turtle_racer.forward(random.randint(1,10))

        if turtle_racer.xcor() >= turtle.window_width() // 2:

            turtle_racer.home()
            turtle_racer.write(turtle_racer.name + ' won!', font=('arial', 24, 'bold'))
            turtle_racer.do_a_360()
            finished = True
            break

turtle.exitonclick()
