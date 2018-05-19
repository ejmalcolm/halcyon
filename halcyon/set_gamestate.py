from planet import Planet
from task import Task
from player import Player
import pickle

Dune = Planet('Dune')
Hoth = Planet('Hoth')

planets = Planet.instances
tasks = Task.instances
players = Player.instances

superlist = [planets, tasks, players]

def save_to_file():
    with open('tags_file.pickle', 'wb') as handle:
        pickle.dump(superlist, handle)

save_to_file()
