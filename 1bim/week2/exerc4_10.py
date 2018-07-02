import turtle


def draw_star(t):
    t.left(36)
    for i in range(0,5):
        t.forward(60)
        t.left(144)
    t.right(36)


tur = turtle.Turtle()

for i in range(1,6):
    draw_star(tur)
    tur.penup()
    tur.left(i*72)
    tur.forward(100)
    tur.right(i*72)
    tur.pendown()

turtle.mainloop()