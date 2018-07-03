from abc import ABC, abstractmethod

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
        return self.areaAlgoBridge.execute()

    def set_areaAlg(self, alg):
        self.areaAlgoBridge = alg
