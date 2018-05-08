import planet
import building
import vehicle
import creature
from tags import get_attributes, get_all_tags

Dune = planet.Planet('Arrakis', 5, 5)

##dont delete above this plzty

#a = building.Building('Forge', Dune, Dune.octants['North'], ['Wood', 'Factory: Wood Crafts'])
#print(a.define_functions())

a = vehicle.SpaceShip('Halcyon', Dune, Dune.octants['North'], 100000)

b = creature.Creature('a', Dune, Dune.octants['North'], 0, 1)
