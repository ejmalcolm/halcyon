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

# Dune = planet.Planet('Arrakis', 5, 5)
#
# ##dont delete above this plzty
#
# bldng = building.Building('Wood Craft Factory', Dune, Dune.octants['North'], ['Refinery: Stone', 'Factory: Wood Crafts'], player.GM)
#
# spcshp = vehicle.SpaceShip('Halcyon', Dune, Dune.octants['North'], 100000)
#
# crtr = creature.Creature('a', Dune, Dune.octants['North'], 0, 1)
#
# labor = creature.Laborer('bob', Dune, Dune.octants['North'], build_rate=5, player=player.GM)
#
# bplan = building.Building_Plan('buh', Dune, Dune.octants['North'], ['Wood', 'Metal'], player.GM)

buh = {'a' : 'b'}

if buh[1] == 'b':
    print(1)
else:
    print(2)
