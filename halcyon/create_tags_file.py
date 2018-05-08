import cpickle as pickle

MATERIAL_TAGS = {}

STRUCTURE_TAGS = {}

FUNCTION_TAGS = {}

def define_a_tag(category, name, list_attributes=[], health=0, work=0):
    if category == 'material':
        MATERIAL_TAGS[name] = {'Attributes' : list_attributes,
                            'Statistics' : {'Health' : health, 'Work' : work}}
    elif category == 'structure':
        STRUCTURE_TAGS[name] = {'Attributes' : list_attributes,
                                'Statistics' : {'Health' : health, 'Work' : work}}
    elif category == 'function':
            FUNCTION_TAGS[name] = {'Attributes' : list_attributes,
                                'Statistics' : {'Health' : health, 'Work' : work}}
    else:
        print('category is incorrect')

define_a_tag('material', 'Wood', ['Flammable', 'Organic'], 10, 1)
define_a_tag('material', 'Stone', health=15, work=3)
define_a_tag('material', 'Metal', ['Electrically Conductive', 'Thermally Conductive'], 20, 5)
define_a_tag('material', 'Iridium', ['Radiation Resistant', 'Electrically Conductive'], 50, 10)
define_a_tag('material', 'Flesh', ['Flammable', 'Organic', 'Decays'], 5, 7)
print)

supertaglist = [MATERIAL_TAGS, STRUCTURE_TAGS, FUNCTION_TAGS]
