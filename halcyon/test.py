from planet import Planet
from building import Building_Plan

hoth = Planet('Hoth', 10, 10)
house_plan = Building_Plan('House', hoth, hoth.octants['North'], ['Wood', 'Enclosed'])

print(house_plan.work_needed)
house_plan.work_on(1)
house_plan.work_on(1)
