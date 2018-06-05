from importlib import import_module
from tags import add_tags

class Object():

    def __init__(self, name, on_planet, in_octant, player):
        self.name = name
        self.player = player
        self.planet = on_planet
        self.octant = in_octant
        #add the object to the contents of the octant
        self.octant.add_occupant(self)
        #initialize the default, blank values for each tag category
        self.tags = {'Material' : [], 'Structure' : [], 'Function' : []}
        self.client_methods = []

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

    def get_stat(self, stat):
        total = 0
        #for each material tag
        for material in self.tags['Material']:
            #get the value of the given stat for each tag
            tag_stat = MATERIAL_TAGS[material]['Statistics'][stat]
            #add it to the total
            total += tag_stat
        #repeat for structure tags
        for structure in self.tags['Structure']:
            tag_stat = STRUCTURE_TAGS[structure]['Statistics'][stat]
            total += tag_stat
        #repeat for function tags
        for function in self.tags['Function']:
            tag_stat = FUNCTION_TAGS[function]['Statistics'][stat]
            total += tag_stat
        return total

    def get_attributes(self):
        attributes = []
        #for each material tag
        for material in self.tags['Material']:
            #get all attributes for each tag
            tag_attributes = MATERIAL_TAGS[material]['Attributes']
            #combine the attributes list with the one being return
            attributes += tag_attributes
        #repeat for structure tags
        for structure in self.tags['Structure']:
            tag_attributes = STRUCTURE_TAGS[structure]['Attributes']
            attributes += tag_attributes
        #repeat for function tags
        for function in self.tags['Function']:
            tag_attributes = FUNCTION_TAGS[function]['Attributes']
            attributes += tag_attributes
        return attributes

    def get_functions(self):
        attributes = get_attributes(self)
        return_list = []
        for attribute in attributes:
            if '|' in attribute:
                    return_list.append(attribute)
        return return_list

    def get_all_tags(self):
        tags = []
        for tag in self.tags['Material'], self.tags['Structure'], self.tags['Function']:
            if tag != []:
                tags += tag
        return tags
