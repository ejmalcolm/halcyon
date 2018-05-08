import planet
import building
from tags import get_attributes, get_all_tags

Dune = planet.Planet('Arrakis', 5, 5)

##dont delete above this plzty

#a = building.Building('Forge', Dune, Dune.octants['North'], ['Wood', 'Factory: Wood Crafts'])
#print(a.define_functions())

list = []

class ex():

    def __init__(self):
        list.append(self)

def create_class(class_name):
    return class_name()

example = create_class(ex)
print(list)
