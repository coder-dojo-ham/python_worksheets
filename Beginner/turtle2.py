from turtle import *

angles = int(input('How many angles do you want? '))

shape('turtle')

turn = 360/angles

for x in range(angles):
    forward(50)
    left(turn)
