import pickle

MATERIAL_TAGS = {}

STRUCTURE_TAGS = {}

FUNCTION_TAGS = {}

def define_a_tag(category, name, list_attributes=[], health=0, work=0, function_slots=0, func_cost=None):
    if category == 'material':
        MATERIAL_TAGS[name] = {'Attributes' : list_attributes,
                            'Statistics' : {'Health' : health, 'Work' : work, 'Functions Slots' : function_slots}}
    elif category == 'structure':
        STRUCTURE_TAGS[name] = {'Attributes' : list_attributes,
                                'Statistics' : {'Health' : health, 'Work' : work, 'Functions Slots' : function_slots}}
    elif category == 'function':
            FUNCTION_TAGS[name] = {'Attributes' : list_attributes,
                                'Statistics' : {'Health' : health, 'Work' : work, 'Functions Slots' : function_slots}}
    else:
        print('category is incorrect')

define_a_tag('material', 'Wood', ['Flammable', 'Organic'], 10, 1)
define_a_tag('material', 'Stone', health=15, work=3)
define_a_tag('material', 'Metal', ['Electrically Conductive', 'Thermally Conductive'], health=20, work=5)
define_a_tag('material', 'Iridium', ['Radiation Resistant', 'Electrically Conductive'], health=50, work=10)
define_a_tag('material', 'Flesh', ['Flammable', 'Organic', 'Decays'], health=5, work=7)

define_a_tag('structure', 'Structure', function_slots=1)
define_a_tag('structure', 'Enclosed', ['Enclosed'], health=3, work=1)
define_a_tag('structure', 'Insulated', ['Insulated'], work=5)
define_a_tag('structure', 'High Walls', ['Secure'], health=10, work=6)
define_a_tag('structure', 'Extra Floor', health=3, work=6, function_slots=1)

define_a_tag('function', 'Factory: Wood Crafts', ['Fabricate|Wood Crafts'], work=3, func_cost='W')
define_a_tag('function', 'Automaton Cradle', ['Spawn|Automaton'])
define_a_tag('function', 'Refinery: Wood', ['Refine|Wooden Log'], work=3, func_cost='W')
define_a_tag('function', 'Refinery: Stone', ['Refine|Stone Brick'], work=6, func_cost='S')
define_a_tag('function', 'Refinery: Metal', ['Refine|Metal Bar'], work=9, func_cost='M')
define_a_tag('function', 'Refinery: Iridium', ['Refine|Iridium'], work=18, func_cost = 'I')


superlist = [MATERIAL_TAGS, STRUCTURE_TAGS, FUNCTION_TAGS]

def save_to_file():
    with open('tags_file.pickle', 'wb') as handle:
        pickle.dump(superlist, handle)

#save_to_file()
