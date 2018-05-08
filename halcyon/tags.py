MATERIAL_TAGS = {
    'Wood' : {'Attributes' : ['Flammable', 'Organic'], 'Statistics' : {'Health' : 10, 'Work' : 1}}
                }

STRUCTURE_TAGS = {
    'Enclosed' : {'Attributes' : ['Enclosed'], 'Statistics' : {'Health' : 3, 'Work' : 1}}
}

FUNCTION_TAGS = {
    'Factory: Wood Crafts' : {'Attributes' : ['Fabricate|Wood Craft'], 'Statistics' : {'Work' : 3}}
}

def add_tags(self, tags):
    for tag in tags:
        if tag in MATERIAL_TAGS:
            self.tags['Material'].append(tag)
        elif tag in STRUCTURE_TAGS:
            self.tags['Structure'].append(tag)
        elif tag in FUNCTION_TAGS:
            self.tags['Function'].append(tag)
        else:
            print("Tag '%s' does not exist" % tag)
            continue

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

def get_all_tags(self):
    tags = []
    for tag in self.tags['Material'], self.tags['Structure'], self.tags['Function']:
        if tag != []:
            tags += tag
    return tags
