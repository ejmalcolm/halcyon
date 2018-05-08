import creature
from planet import Planet

Dune = Planet('Arrakis', 5, 5)

Jon = creature.Automaton('Jon', on_planet=Dune, in_octant=Dune.octants['North'])
