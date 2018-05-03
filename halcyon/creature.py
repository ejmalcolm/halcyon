class Creature():

    def __init__(self, name, on_planet, in_octant, health=5, move=0, player=0):
        self.name = name
        self.health = health
        self.move = move
        self.player = player
        self.planet = on_planet
        self.octant = in_octant
        self.octant.add_occupant(self)

    def __str__(self):
        return 'a Creature named %s' % self.name

class Laborer(Creature):

    def __init__(self, name, on_planet, in_octant, harvest_rate=0, build_rate=0):
        super().__init__(name, on_planet, in_octant, move=1/5, health=5)
        self.harvest_rate = harvest_rate
        self.build_rate = build_rate

    def __str__(self):
        return 'a Laborer named %s' % self.name

    def harvest_resource(self, resource):
        octant = self.octant
        if resource in octant.resources:
            return '%s is now harvesting %s' % (self.name, resource)
        return 'there is no %s in %s' % (resource, self.octant)

class Crew_Member(Laborer):

    def __init__(self, name, on_planet, in_octant, role):
        super().__init__(name, on_planet, in_octant, harvest_rate=1/12)
        self.role = role

class Automaton(Laborer):

    def __init__(self, name, on_planet, in_octant):
        super().__init__(name, on_planet, in_octant, harvest_rate=1/6, build_rate=1/3)
