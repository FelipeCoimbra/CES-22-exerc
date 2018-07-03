class Polygon:
    '''
        Class for a 2D Polygon. A n-agon is constructed from a vector list with
        n+1 vertices where the last vertex is equal to the first one.
    '''

    def __init__(self, vlist):
        if len(vlist) < 3:
            raise ValueError()

        self.vlist = vlist
        self.areaAlgoBridge = None

    def area(self):
        if self.areaAlgoBridge is None:
            return 0.0
        return self.areaAlgBridge.execute()

    def set_areaAlg(self, alg):
        self.areaAlgoBridge = alg

class PolygonFactory:
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
        return vertices

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
