from object import Object
from tags import add_tags
from task import Task

class Creature(Object):

    def __init__(self, name, on_planet, in_octant, player, move):
        super().__init__(name, on_planet, in_octant, player)
        self.move = move

    def __str__(self):
        return 'a Creature named %s' % self.name

class Laborer(Creature):

    def __init__(self, name, on_planet, in_octant, player=0, harvest_rate=0, build_rate=0):
        super().__init__(name, on_planet, in_octant, player, move=1/5)
        self.harvest_rate = harvest_rate
        self.build_rate = build_rate

    def __str__(self):
        return 'a Laborer named %s' % self.name

    def harvest_resource(self, resource):
        '''starts a Task() of harvesting the given resource if the resource is in the same octant'''
        #check if the resource is in the same octant
        if resource in self.octant.resources:
            #calculate the number of hours needed to finish the Task
            hours = (1/self.harvest_rate)
            #start the Task()
            harvest_task = Task(self, hours, self.player.gain_resource(resource))
            #report what's been done
            return '%s is now harvesting %s' % (self.name, resource)
        return 'there is no %s in %s' % (resource, self.octant)

    def construct_building(self, building_plan):
        '''starts a task of building the given plan if the plan is in the same octant'''
        if building_plan in self.octant.contents:
            #hours needed to finish the task
            hours = (1/self.build_rate)
            #start the Task()
            build_task = Task(self, hours, building_plan.plan_finished())
            #report what's been done
            return '%s is now building %s' % (self.name, building_plan)
        return 'there is no unfinished %s in %s' % (building_plan, self.octant)

class CrewMember(Laborer):

    def __init__(self, name, on_planet, in_octant, player):
        super().__init__(name, on_planet, in_octant, harvest_rate=1/12)
        #add the Flesh material to the material tags
        add_tags(self, ['Flesh'])

class Engineer(CrewMember):

    def make_building_plan(self):
        return self.octant

class Soldier(CrewMember):
    pass

class Researcher(CrewMember):
    pass

class Artist(CrewMember):
    pass

class Automaton(Laborer):

    def __init__(self, name, on_planet, in_octant, player):
        super().__init__(name, on_planet, in_octant, harvest_rate=1/6, build_rate=1/3)
        add_tags(self, ['Metal'])
