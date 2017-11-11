import turtle

def shape(angles, length=50, shape='turtle'):

    turtle.shape(shape)

    turn = 360/angles

    for _ in range(angles):
        turtle.forward(length)
        turtle.left(turn)
