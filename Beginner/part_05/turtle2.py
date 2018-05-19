import turtle

turns = [90, 90, 90, 90, -90, -90, -90, -90]

turtle.shape('turtle')

for turn in turns:
    turtle.forward(40)
    turtle.left(turn)
