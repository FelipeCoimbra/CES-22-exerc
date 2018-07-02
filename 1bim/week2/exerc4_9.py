import turtle


def draw_star(t):
    t.left(36)
    for i in range(0,5):
        t.forward(60)
        t.left(144)
    t.right(36)


tur = turtle.Turtle()
draw_star(tur)

turtle.mainloop()