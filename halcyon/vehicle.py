from object import Object

class Vehicle(Object):

    def __init__(self, name, on_planet, in_octant, move=0, player=0, terrain='Terrestial'):
        super().__init__(name, on_planet, in_octant, player=player)
        self.move = move
        self.terrain = terrain

class SpaceShip(Vehicle):

    def __init__(self, name, on_planet, in_octant, space_move_miles, player=0):
        super().__init__(name, on_planet, in_octant, player, terrain='Space')
        self.spmove = space_move_miles
        is_operable = bool(self.planet == 'Space')

class Halcyon(SpaceShip):

    def __init__(self, on_planet, in_octant, player):
        super().__init__('Halcyon', on_planet, in_octant, 100000, player)
        add_tags(self, tags_list=['Iridium', 'Unique|Cryogenic Chamber',
                                'Unique|Incubator', 'Spawn|Automaton',
                                'Unique|CSAT', 'Unique|Inspect Planet'])
