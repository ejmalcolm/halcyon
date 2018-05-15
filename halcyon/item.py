from object import Object

class Item(Object):

    def __init__(self, name, on_planet, in_octant, tags, type):
        super().__init__(name, on_planet, in_octant, tags, player=None)
        self.type = type
