import random
from collections import Counter, namedtuple

# A planet has eight octants: NW, N, NE, E, SE, S, SW, W
# Each octant has a biome type: aquatic, desert, forest, grassland, tundra, hills
# Each octant has up to five resources assigned to it
# Can simply have no Resources
# Natural Resources, more common, are wood, stone, and metal
# Non-Standard Resources are very unique
# The resources within a biome are influenced by the biome type

def unique_chance():
    #figure out how to make this about 1 in 8
    randint = random.randint(1, 8)
    if randint == 7:
        return 'unique'
    return 'none'

CARDINAL_DIRECTIONS = ('North', 'East', 'South', 'West', 'Northeast', 'Northwest', 'Southeast', 'Southwest')
BIOMES = ('aquatic', 'aquatic', 'desert', 'forest', 'grassland', 'tundra', 'hills')
RESOURCE_DISTRIBUTION = {
    'aquatic': ('none', 'none', 'Stone', unique_chance(), unique_chance()),
    'desert': ('none', 'none', 'Stone', 'Stone', unique_chance()),
    'forest': ('none', 'none', 'Wood', 'Wood', unique_chance()),
    'grassland': ('none', 'none', 'Stone', 'Wood', unique_chance()),
    'tundra': ('none', 'none', 'Metal', 'Metal', unique_chance()),
    'hills': ('none', 'none', 'Stone', 'Metal', unique_chance())
}


def resource_in(biome):
    #Gets five random resources based on the biome.
    resources = []
    for _ in range(5):
        resource = random.choice(RESOURCE_DISTRIBUTION[biome])
        if resource != 'none':
            resources.append(resource)
    return sorted(resources, reverse=True)

def random_biome():
    return random.choice(BIOMES)

def does_civilization_exist():
    randint = random.randint(1, 7)
    return bool(randint == 7)

class Civilization():

    def __init__(self, tier, status):
        self.tier = tier
        self.status = status

    def __str__(self):
        return 'a civilization of tier %d' % self.tier

    def change_tier(self, tier):
        self.tier = tier

    def change_status(self, status):
        self.status = status

class Octant():

    def __init__(self, name, planet):
        self.name = name
        self.biome = random_biome()
        self.resources = resource_in(self.biome)
        self.contents = []
        self.civilization = None
        if does_civilization_exist():
            self.civilization = Civilization(tier=random.randint(1, 5), status='Neutral')
            self.contents.append(self.civilization)
        self.planet = planet

    def __str__(self):
        return 'the %s octant of %s' % (self.name, self.planet)

    def add_occupant(self, occupant):
        self.contents.append(occupant)

class Planet():

    instances = []

    def __init__(self, name):
        #add self to instances for gamestate purposes
        self.__class__.instances.append(self)
        #rest of init
        self.name = name
        octants = {}
        for direction in CARDINAL_DIRECTIONS:
            octants[direction] = Octant(name=direction, planet=self)
        self.octants = octants
        #set the usable methods for the GUI
        self.client_methods = (
                                ('Get description', self.get_description, None),
                                ('Get octant biome', self.get_octant_biome, CARDINAL_DIRECTIONS)
        )

    def __str__(self):
        return 'a planet named %s' % self.name

    def get_octant_biome(self, octant_name):
        octant = self.octants[octant_name]
        return 'The %s octant is a %s biome' % (octant_name, octant.biome)

    def get_description(self):
        '''Generates a description of the planet based on the most common biome'''
        planet_biomes = []
        for octant in CARDINAL_DIRECTIONS:
            octant_biome = self.octants[octant].biome
            planet_biomes.append(octant_biome)
        cnt = Counter(planet_biomes)
        most_common_biome = cnt.most_common(1)[0][0]
        return '%s is a mostly %s planet.' % (self.name, most_common_biome)
