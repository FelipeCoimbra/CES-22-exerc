from abc import ABC, abstractmethod
from structures.polygon import Polygon

class BaseFactory(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        pass

class PolygonFactory(BaseFactory):
    '''
        Class for a 2D Polygon Factory. You may create polygons from lists
        of tuples or directly from tuples
    '''
    def __init__(self, *args):
        pass

    def from_list(self, vlist):
        if self.__validate_vlist(vlist):
            return Polygon(vlist)
        else:
            raise ValueError()

    def from_tuples(self, *args):
        vertices = []
        for arg in args:
            vertices.append(arg)
        if not self.__validate_vlist(vertices):
            raise ValueError()
        return Polygon(vertices)

    def create(self, *args):
        return self.from_tuples(args)

    def __validate_vlist(self, vlist):
        if type(vlist) is list and len(vlist) > 3: # Remember the list is cyclic
            for v in vlist:
                if not self.__validate_tuple(v):
                    return False
            return True

        return False

    def __validate_tuple(self, vertex):
        return type(vertex) is tuple and len(vertex) == 2
