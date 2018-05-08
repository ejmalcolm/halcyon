from tags import add_tags

class Object():

        def __init__(self, name, on_planet, in_octant, player, tags=[]):
            self.name = name
            self.player = player
            self.planet = on_planet
            self.octant = in_octant
            #add the object to the contents of the octant
            self.octant.add_occupant(self)
            #initialize the default, blank values for each tag category
            self.tags = {'Material' : [], 'Structure' : [], 'Function' : []}
            #send the tag argument to the add_tags function
            add_tags(self, tags)
