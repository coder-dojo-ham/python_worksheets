import turtle

turns = [10, 20, 30, 30, 0, 0, 10, 30, 30, 20, 0, 20, 30, 30, 10, 0, 0, 30, 30, 20, 10, -90, 0, -90, 0, -90, 0, 0]

turtle.shape('turtle')

for turn in turns:
    turtle.forward(40)
    turtle.left(turn)
