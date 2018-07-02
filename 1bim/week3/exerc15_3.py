from math import fabs

class Point:


    EPS = 0.00001

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_string(self):
        return "({0}, {1})".format(self.x, self.y)


    @classmethod
    def midpoint(cls, p1, p2):
        """ Return the midpoint of points p1 and p2 """
        mx = (p1.x + p2.x) / 2
        my = (p1.y + p2.y) / 2
        return Point(mx, my)

    def slope_from_origin(self):
        return self.y/self.x


