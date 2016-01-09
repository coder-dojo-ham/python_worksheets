from turtle import *


shape('turtle')
def shape_left(angles):
    turn = 360/angles

    for x in range(angles):
        forward(50)
        left(turn)

def shape_right(angles):
    turn = 360/angles

    for x in range(angles):
        forward(50)
        right(turn)
