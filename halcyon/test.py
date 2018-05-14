import planet
import building
import vehicle
import creature
import tags

Dune = planet.Planet('Arrakis', 5, 5)

##dont delete above this plzty

a = building.Building('Wood Craft Factory', Dune, Dune.octants['North'], ['Refinery: Stone', 'Factory: Wood Crafts'])

c = vehicle.SpaceShip('Halcyon', Dune, Dune.octants['North'], 100000)

b = creature.Creature('a', Dune, Dune.octants['North'], 0, 1)

z = a.use_function('Spawn|Automaton')
print(z)
