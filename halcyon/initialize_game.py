from creature import Automaton
from planet import Planet, Octant
from task import ACTIVE_TASKS
from player import Player, GM
import dill as pickle

###Stuff that needs to be added at the start of game goes here
Dune = Planet('Dune')
Alpha = Automaton('Alpha', Dune, Dune.octants['North'], GM)



###
planets = {planet.name: planet for planet in Planet.instances}
tasks = {str(task): task for task in ACTIVE_TASKS}
players = {str(player): player for player in Player.instances}

superlist = [planets, tasks, players]

def save_to_file():
    with open('gamestate.pickle', 'wb') as handle:
        pickle.dump(superlist, handle)

if __name__ == '__main__':
    print('Gamestate file written.')
    save_to_file()
