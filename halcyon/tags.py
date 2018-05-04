MATERIAL_TAGS = {
    'Wood' : {'Attributes' : ['Flammable', 'Organic'], 'Statistics' : [10, 1]}
                }

STRUCTURE_TAGS = {
    'Enclosed' : {'Attributes' : ['Enclosed'], 'Statistics' : [3, 1]}
}

FUNCTION_TAGS = {
    'Factory: Wood Craft' : {'Attributes' : ['Create Wood Craft'], 'Statistics' : [0, 3]}
}

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
