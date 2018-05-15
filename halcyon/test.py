import planet
import building
import vehicle
import creature
import tags
import player
import task

Dune = planet.Planet('Arrakis', 5, 5)
GM = player.Player('gamemaster', 0)

##dont delete above this plzty

a = building.Building('Wood Craft Factory', Dune, Dune.octants['North'], ['Refinery: Stone', 'Factory: Wood Crafts'])

c = vehicle.SpaceShip('Halcyon', Dune, Dune.octants['North'], 100000)

b = creature.Creature('a', Dune, Dune.octants['North'], 0, 1)

lab = creature.Laborer('bob', Dune, Dune.octants['South'], harvest_rate=5)
