from planet import Planet

MATERIAL_TAGS = {
    'Wood' : {'Attributes' : ['Flammable', 'Organic'], 'Statistics' : [10, 1]}
                }

class Building_Plan():

    def __init__(self, name, on_planet, in_octant, tags, player=0):
        self.name = name
        self.player = player
        self.planet = on_planet
        self.octant = in_octant
        #Add the building plan to the contents of the octant
        self.octant.add_occupant(self)
        #initialize the default, blank values for each tag category
        self.tags = {'Material' : [], 'Structure' : [], 'Function' : []}
        self.material = None
        self.structure = None
        self.function = None
        #send the tag argument to the add_tags function
        add_tags(tags)

    def __str__(self):
        return 'a building plan for a %s' % self.name

    def add_tags(self, tags):
        for tag in tags:
            if tags

Arrakis = Planet('Arrakis', 5, 5)
House = Building_Plan('House', Arrakis, Arrakis.octants['North'], ['Wood', 'Enclosed'])

#print(House.material)