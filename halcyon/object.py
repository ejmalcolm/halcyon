from importlib import import_module
from tags import add_tags, get_functions

class Object():

    def __init__(self, name, on_planet, in_octant, player=0):
        self.name = name
        self.player = player
        self.planet = on_planet
        self.octant = in_octant
        #add the object to the contents of the octant
        self.octant.add_occupant(self)
        #initialize the default, blank values for each tag category
        self.tags = {'Material' : [], 'Structure' : [], 'Function' : []}

    def use_function(self, function):
        #splits the given function into a category of function and a specific event
        category = function.split('|')[0]
        specific = function.split('|')[1]
        #if the category is spawn, create an instance of the specific class
        #the initalizations of the class handles all of the rest
        if category == 'Spawn':
            #name = input('Enter name of creature')
            Needed_Class = getattr(import_module('creature'), specific)
            spawned_creature = Needed_Class(specific, self.planet, self.octant, self.player)
            return '%s has been created by %s' % (spawned_creature, self)
        elif category == 'Fabricate':
            pass
        elif category == 'Refine':
            pass
        elif category == 'Produce':
            pass
        elif category == 'Unique':
            pass
