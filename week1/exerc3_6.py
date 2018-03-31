import turtle


def make_polygon(tur, nsides):
    if tur is None or nsides < 3:
        raise ValueError()
    turn_angle = 360/nsides
    for i in range(0,nsides):
        tur.left(turn_angle)
        tur.forward(100)


t = turtle.Turtle()

## Equilateral Triangle
# sides = 3

## Square
# sides = 4

## Hexagon
# sides = 6

## Octagon
sides = 8

make_polygon(t,sides)

turtle.mainloop()
