from abc import ABC, abstractmethod
from math import sqrt, fabs
from structures.polygon import Polygon

class PolygonAreaAlgBridge(ABC):
    '''
        This is the abstract baseclass interface
        This class decouples implementation of the area algorithm
    '''
    def __init__(self, polygon=None):
        self.polygon = polygon

    @abstractmethod
    def bind(self, new_polygon):
        self.polygon = new_polygon

    @abstractmethod
    def execute(self):
        raise NotImplementedError('You must override area algorithm execution')

class OnlyTriangleAreaAlg(PolygonAreaAlgBridge):
    '''
        This algorithm only works if the polygon is a triangle but it is fast
    '''
    def __init__(self, polygon):
        super(OnlyTriangleAreaAlg, self).__init__(polygon)

    def execute(self):
        v1 = self.polygon.vlist[0]
        v2 = self.polygon.vlist[1]
        v3 = self.polygon.vlist[2]
        l1 = (v2[0]-v1[0], v2[1]-v1[1])
        l2 = (v3[0]-v1[0], v3[1]-v1[1])
        cross = (0, 0, l1[0]*l2[1]-l1[1]*l2[0])
        area = sqrt(cross[0]**2 + cross[1]**2 + cross[2]**2)/2
        return fabs(area)

class GeneralAreaAlg(PolygonAreaAlgBridge):
    '''
        This algorithm has higher complexity but work for any 2d polygon
    '''
    def __init__(self, polygon):
        super(GeneralAreaAlg, self).__init__(polygon)

    def execute(self):
        vertices = self.polygon.vlist
        area = 0.0
        for i in range(0, len(vertices)-3):
            area += self.__calc_triang_area(vertices[i], vertices[i+1], vertices[i+2])
        return fabs(area)

    def __calc_triang_area(self, v1, v2, v3):
        l1 = (v2[0]-v1[0], v2[1]-v1[1])
        l2 = (v3[0]-v1[0], v3[1]-v1[1])
        cross = (0, 0, l1[0]*l2[1]-l1[1]*l2[0])
        area = sqrt(cross[0]**2 + cross[1]**2 + cross[2]**2)/2
        return area

# Making us some pretty triangle
poly = Polygon([(0,0), (0.866, 0.5), (1,0)])

# Wanna know its area. Bridge will call specific area function
poly.set_areaAlg(OnlyTriangleAreaAlg(poly))
print(poly.area())

# Now it's some messed up non-convex polygon. Ouch
poly = Polygon([(0,0), (1,0), (2,1), (3,4), (3,5), (2,2), (1,2), (0,0)])

# Need new algorithm for that
poly.set_areaAlg(GeneralAreaAlg(poly))
print(poly.area())
