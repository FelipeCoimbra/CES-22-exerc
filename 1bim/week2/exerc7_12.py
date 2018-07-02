import turtle
from turtle import Turtle
from math import sqrt

t = Turtle()

steps = [(100, 135), (100*sqrt(2), 285), (100, 240), (100, 240), (100, 90), (100, 135), (100*sqrt(2), 225), (100, 0)]

for step in steps:
    t.forward(step[0])
    t.left(step[1])

turtle.mainloop()