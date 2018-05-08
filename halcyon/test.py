import planet
import building
from tags import get_attributes, get_all_tags

Dune = planet.Planet('Arrakis', 5, 5)

##dont delete above this plzty

a = building.Building('Forge', Dune, Dune.octants['North'], ['Wood', 'Factory: Wood Crafts'])
a.get_functions()
