'''
    Decorator Pattern. Extend functionalities of classes without touching in their
    internal structure by adding a wrapper class (called Decorator Class)
'''

## Our current Polygon class does not have checking methods to assure vertices
##      lists given in their construction are correct. Lets add that with
##      the use of the Decorator Pattern

from structures.polygon import Polygon

class DecoratedPolygon:

    def __init__(self, vlist):
        corrected_vlist = self.__correct(vlist)
        self.polygon = Polygon(corrected_vlist)

    def area(self):
        return self.polygon.area()

    def set_areaAlg(self, alg):
        self.polygon.set_areaAlg(alg)

    def __correct(self, vlist):
        if vlist[-1] != vlist[0]:
            vlist.append(vlist[0])
