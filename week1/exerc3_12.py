from turtle import Turtle
import turtle

ts = []
l = 100
offset = 20
t_center = Turtle()

for i in range(0,12):
    t = Turtle()
    t.penup()
    t.left(360*i/12)
    t.forward(l)
    t.pendown()
    t.forward(offset)
    t.penup()
    t.forward(offset/2)
    ts.append(t)

turtle.mainloop()

