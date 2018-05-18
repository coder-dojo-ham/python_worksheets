import turtle

turtle.shape('turtle')


def shape(angles):
    turn = 360/angles

    for _ in range(angles):
        turtle.forward(50)
        turtle.left(turn)
