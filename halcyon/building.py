from planet import Planet

MATERIAL_TAGS = {
    'Wood' : {'Attributes' : ['Flammable', 'Organic'], 'Statistics' : [10, 1]}
                }

STRUCTURE_TAGS = {
    'Enclosed' : {'Attributes' : ['Enclosed'], 'Statistics' : [3, 1]}
}

FUNCTION_TAGS = {}

def add_tags(self, tags):
    for tag in tags:
        if tag in MATERIAL_TAGS:
            self.material.append(tag)
        elif tag in STRUCTURE_TAGS:
            self.structure.append(tag)
        elif tag in FUNCTION_TAGS:
            self.function.append(tag)
        else:
            print("Tag '%s' does not exist" % tag)
            continue

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
        self.material = []
        self.structure = []
        self.function = []
        #send the tag argument to the add_tags function
        add_tags(self, tags)

    def __str__(self):
        return 'a building plan for a %s' % self.name

Arrakis = Planet('Arrakis', 5, 5)
House = Building_Plan('House', Arrakis, Arrakis.octants['North'], ['Wood', 'Enclosed', 'fuck'])

#print(House.material)
