import turtle
import random

scrn = turtle.Screen()

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.penup()
t1.left(90)
t1.forward(50)
t1.right(90)
t1.pendown()

t1_pos = 0

t2_pos = 0

while t1_pos < 350 and t2_pos < 350:
    t1_mover = random.randint(0, 20)
    t2_mover = random.randint(0,20)
    t1_pos += t1_mover
    t2_pos += t2_mover
    t1.forward(t1_mover)
    t2.forward(t2_mover)
