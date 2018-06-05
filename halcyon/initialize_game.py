from creature import Automaton, Engineer
from planet import Planet, Octant
from task import ACTIVE_TASKS
from player import Player, GM
import dill as pickle
from random import sample

###Define the Demutatio system
random_planet_names = ['Soskuter', 'Foplauhines', 'Koswuna', 'Ablarvis', 'Jeunerth',
                       'Soethea', 'Skujohines', 'Frokelara', 'Slomia', 'Glinda 2SO',
                       'Afluynia', 'Obroepra', 'Soslosie', 'Ucloria', 'Eahines',
                       'Beiria', 'Shevunia', 'Sanctuary', 'Guardhome', 'Red 229',
                       'Belfry', 'Mortis', 'Cale', 'Lost', 'Swell', 'Violet 490',
                       'Gaia', 'Arrakis', 'Hoth', 'Yavin', 'Cadia', 'Indigo 10']
names = sample(random_planet_names, 5)

def save_to_file():
    planets = {planet.name: planet for planet in Planet.instances}
    tasks = {str(task): task for task in ACTIVE_TASKS}
    players = {str(player): player for player in Player.instances}
    superlist = [planets, tasks, players]
    with open('gamestate.pickle', 'wb') as handle:
        pickle.dump(superlist, handle)

if __name__ == '__main__':
    ##initial gamestate
    PlanetA = Planet(names[0])
    PlanetB = Planet(names[1])
    PlanetC = Planet(names[2])
    PlanetD = Planet(names[3])
    PlanetE = Planet(names[4])
    ##debug stuff
    Dune = Planet('Dune')
    Alpha = Automaton('Alpha', Dune, Dune.octants['North'], GM)
    Beta = Engineer('Beta', Dune, Dune.octants['North'], GM)
    ##write the pickle file
    print('Gamestate file written.')
    save_to_file()
