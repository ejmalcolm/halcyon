from object import Object
from player import GM
from tags import add_tags
from planet import Planet

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
        self.planets_needed = Planet.instances
        self.names_of_planets = [planet.name for planet in Planet.instances]
        self.client_methods.append(('Move to Planet', self.move_to_planet, self.names_of_planets, True))
        # self.client_methods.extend(
        #                             (('Cryogenic Chamber',),
        #                             ('Incubator',),
        #                             ('Research Lab',),
        #                             ('CSAT',))
        #                             )

    def move_to_planet(self, dest_planet_name):
        try:
            target_planet = [planet if planet.name == dest_planet_name else None for planet in Planet.instances][0]
        except Exception as e:
            print(e)
        #current_pos = self.planet.pos
        #target_pos = dest_planet.pos
        return '%s is moving to %s' % (self, dest_planet_name)

    def __str__(self):
        return "%s's Halcyon" % self.player
