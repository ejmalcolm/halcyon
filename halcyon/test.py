import planet
import building

Dune = planet.Planet('Arrakis', 5, 5)

x = building.Building_Plan('Forge', Dune, Dune.octants['North'], ['Wood'])

x.plan_finished()

a = Dune.octants['North'].contents
print(a)
