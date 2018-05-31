from planet import Planet, Octant
from task import ACTIVE_TASKS
from player import Player
import dill as pickle

Space = Planet('Space')
Space.octants = ['Void']

Dune = Planet('Dune')

planets = {planet.name: planet for planet in Planet.instances}
tasks = {str(task): task for task in ACTIVE_TASKS}
players = {str(player): player for player in Player.instances}

superlist = [planets, tasks, players]

def save_to_file():
    with open('gamestate.pickle', 'wb') as handle:
        pickle.dump(superlist, handle)

save_to_file()
