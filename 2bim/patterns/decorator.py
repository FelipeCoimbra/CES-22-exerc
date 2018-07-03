'''
    Decorator Pattern. Extend functionalities of classes without touching in their
    internal structure by adding a wrapper class (called Decorator Class)
'''

## Our current Polygon class does not have checking methods to assure vertices
##      lists given in their construction are correct. Lets add that with
##      the use of the Decorator Pattern

from structures.polygon import Polygon
from bridge import GeneralAreaAlg

class DecoratedPolygon:

    def __init__(self, vlist):
        corrected_vlist = self.__correct(vlist)
        self.polygon = Polygon(corrected_vlist)

    @property
    def vlist(self):
        return self.polygon.vlist

    def area(self):
        return self.polygon.area()

    def set_areaAlg(self, alg):
        self.polygon.set_areaAlg(alg)

    def __correct(self, vlist):
        new_vlist = vlist
        if new_vlist[-1] != new_vlist[0]:
            new_vlist.append(new_vlist[0])
        return new_vlist

if __name__ == "__main__":
    poly = DecoratedPolygon([(0,0), (0,1), (1,1), (1,0)]) # wrong construction
    poly.set_areaAlg(GeneralAreaAlg(poly))
    print(poly.area()) # but its still ok
