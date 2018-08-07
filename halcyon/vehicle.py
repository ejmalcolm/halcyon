from object import Object
from player import GM
from tags import add_tags
from planet import Planet
from task import Task

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
        self.planets_avail = Planet.instances
        self.names_of_planets = [planet.name for planet in Planet.instances]
        self.client_methods.append(('Move to Planet', self.move_to_planet, self.names_of_planets, True))
        # self.client_methods.extend(
        #                             (('Cryogenic Chamber',),
        #                             ('Incubator',),
        #                             ('Research Lab',),
        #                             ('CSAT',))
        #                             )

    def move_to_planet(self, dest_planet_name):
        #get the target planet class object
        for planet in self.planets_avail:
            if planet.name == dest_planet_name:
                target_planet = planet
                target_pos = planet.pos
        current_pos = self.planet.pos
        if current_pos == target_pos:
            return '%s is already on %s' % (self, dest_planet_name)
        distance = abs(current_pos - target_pos)
        travel_time = distance*18.5
        task_time = Task(
                        self, travel_time,
                        self.arrive_at_planet, self.player,
                        arguments=[planet], 
                        result= '%s has arrived at %s.' % (self, dest_planet_name))
        print(travel_time)
        return '%s is moving to %s' % (self, dest_planet_name)

    def arrive_at_planet(self, arrival_planet):
        pass

    def __str__(self):
        return "%s's Halcyon" % self.player
