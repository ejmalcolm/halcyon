import planet
import building

from tags import get_attributes, get_all_tags
Dune = planet.Planet('Arrakis', 5, 5)

x = building.Building_Plan('Forge', Dune, Dune.octants['North'], ['Wood'])

a = x.plan_finished()
print(get_attributes(a))
