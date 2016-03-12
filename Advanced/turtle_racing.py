import turtle


class TurtleRacer(turtle.Turtle):
    def __init__(self, name, *args, **kwargs):
        super(TurtleRacer, self).__init__(*args, **kwargs)
        self.name = name

    def speak(self):
        print("Hi my name is " + self.name)

    def do_a_360(self):
        self.left(360)

    def do_a_180(self):
        self.right(180)

    def make_a_shape(self, angles):
        turn = 360/angles

        for _ in range(angles):
            self.forward(50)
            self.left(turn)


screen = turtle.Screen()

turtle1 = TurtleRacer('Donatello')

turtle2 = TurtleRacer('Leonardo')

turtle2.penup()

turtle2.right(90)
turtle2.forward(100)
turtle2.left(90)

turtle2.pendown()

turtle.exitonclick()