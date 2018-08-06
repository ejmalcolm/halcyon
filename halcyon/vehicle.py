from object import Object
from player import GM
from tags import add_tags

class Vehicle(Object):

    def __init__(self, name, on_planet, in_octant, move=0, player=GM, terrain='Terrestial'):
        super().__init__(name, on_planet, in_octant, player=player)
        self.move = move
        self.terrain = terrain

class SpaceShip(Vehicle):

    def __init__(self, name, on_planet, in_octant, space_move_miles, player=GM):
        super().__init__(name, on_planet, in_octant, player, terrain='Space')
        self.spmove = space_move_miles
        is_operable = bool(self.planet.name == 'Space')

class Halcyon(SpaceShip):

    def __init__(self, on_planet, in_octant, player):
        super().__init__("%s's Halcyon" % player, on_planet, in_octant, 100000, player)
        add_tags(self, tags_list=['Iridium', 'Automaton Cradle'])
        # self.client_methods.extend(
        #                             (('Cryogenic Chamber',),
        #                             ('Incubator',),
        #                             ('Research Lab',),
        #                             ('CSAT',))
        #                             )

    def __str__(self):
        return "%s's Halcyon" % self.player
