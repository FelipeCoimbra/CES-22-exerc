'''
    AbstractFactory: A way of descentralizing object creation to proper factories
    while
'''
from structures.polygon import Polygon, PolygonFactory

class AbstractFactory:

    def __init__(self):
        self.factories = {}

    def registerFactory(self, key, factory):
        self.factories[key] = factory

    def getFactory(self, key):
        return self.factories.get(key)

    def create(self, key, *args):
        factory = self.factories.get(key)
        if factory is None:
            return None
        return factory.create(args)

creator = AbstractFactory()
creator.registerFactory("polygon", PolygonFactory())

# Two ways of creating polygon instances from factory
# 1) Directly ask an object passing proper args to the common interface
polygonA = creator.create("polygon", (0,0), (0,1), (1,1), (1,0), (0,0) )

# 2) Ask for the factory itself to use a specific interface
polygonFac = creator.getFactory("polygon")
polygonB = polygonFac.from_list([(0,0), (0,1), (1,1), (1,0), (0,0)])
