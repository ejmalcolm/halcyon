import dill as pickle
import pika
import planet
import building
import vehicle
import creature
import tags
import player
import task
import inspect
from collections import namedtuple
import datetime
import dill as pickle

Dune = planet.Planet('Arrakis')
Arrakis = planet.Planet('Hoth')

##dont delete above this plzty

# bldng = building.Building('Wood Craft Factory', Dune, Dune.octants['North'], ['Refinery: Stone', 'Factory: Wood Crafts'], player.GM)
#
# spcshp = vehicle.SpaceShip('Halcyon', Dune, Dune.octants['North'], 100000)
#
# crtr = creature.Creature('a', Dune, Dune.octants['North'], 0, 1)
#
# labor = creature.Laborer('bob', Dune, Dune.octants['North'], build_rate=5, player=player.GM)
#
# bplan = building.BuildingPlan('buh', Dune, Dune.octants['North'], ['Wood', 'Metal'], player.GM)

#with open('gamestate.pickle', 'wb') as handle:
#    pickle.dump(planet.Planet.instances, handle)

print(Dune.instances)

with open('gamestate.pickle', 'rb') as handle:
    a = pickle.load(handle)
    for object in a:
        planet.Planet.instances.append(object)

print(planet.Planet.instances)
