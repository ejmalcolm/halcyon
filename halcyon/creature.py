from object import Object
from tags import add_tags
from task import Task
from building import BuildingPlan

class Creature(Object):

    def __init__(self, name, on_planet, in_octant, player, move):
        super().__init__(name, on_planet, in_octant, player)
        self.move = move
        #used as a way to check if the creature is currently doing a task
        self.busy = False

    def __str__(self):
        return 'Creature named %s' % self.name

class Laborer(Creature):

    def __init__(self, name, on_planet, in_octant, player, harvest_rate=0, build_rate=0):
        super().__init__(name, on_planet, in_octant, player, move=1/5)
        self.harvest_rate = harvest_rate
        self.build_rate = build_rate
        self.client_methods.append(('Harvest Resource', self.harvest_resource,
                                    self.octant.resources, True))
        self.client_methods.append(('Construct Building', self.construct_building,
                                    self.octant.class_objects_in('BuildingPlan'), True))

    def __str__(self):
        return 'Laborer named %s' % self.name

    def harvest_resource(self, resource):
        '''starts a Task() of harvesting the given resource if the resource is in the same octant'''
        if self.busy:
            return '%s is already occupied' % self.name
        #check if the resource is in the same octant
        if resource in self.octant.resources:
            #calculate the number of hours needed to finish the Task
            try:
                hours = (1/self.harvest_rate)
            except:
                return 'harvesting rate of %s is zero' % self
            #start the Task()
            result = '%s gains 1 %s' % (self.player, resource)
            harvest_task = Task(self, hours, self.player.gain_resource, self.player,
                                arguments=[resource], result = 'Gain %s' % resource)
            #report what's been done
            return '%s harvests %s' % (self.name, resource)
        return 'there is no %s in %s' % (resource, self.octant)

    def construct_building(self, building_plan):
        '''starts a task of building the given plan if the plan is in the same octant'''
        if self.busy:
            return '%s is already occupied' % self.name
        if building_plan in self.octant.contents:
            #check if the needed resource is available
            resource_check = all(resources in building_plan.resource_needed for resources in self.player.resources)
            if resource_check:
                #hours needed to finish the task
                try:
                    hours = (1/self.build_rate)
                except:
                    return 'building rate of %s is zero' % self
                #start the Task()
                build_task = Task(self, hours, building_plan.work_on,
                                    self.player, arguments=[1],
                                    result = '%s constructs %s' % (self, building_plan))
                #report what's been done
                return '%s constructing %s' % (self.name, building_plan)
        return '%s in %s is not constructable' % (building_plan, self.octant)

class CrewMember(Laborer):

    def __init__(self, name, on_planet, in_octant, player):
        super().__init__(name, on_planet, in_octant, player, harvest_rate=1/12)
        #add the Flesh material to the material tags
        add_tags(self, ['Flesh'])

class Engineer(CrewMember):

    def __init__(self, name, on_planet, in_octant, player):
        super().__init__(name, on_planet, in_octant, player)
        #self.client_methods.append(('Create Building Plan'))

    def make_building_plan(self, name, tags):
        created_plan = BuildingPlan(name, self.planet, self.octant, tags, self.player)

class Soldier(CrewMember):
    pass

class Researcher(CrewMember):
    pass

class Artist(CrewMember):
    pass

class Automaton(Laborer):

    def __init__(self, name, on_planet, in_octant, player):
        super().__init__(name, on_planet, in_octant, player, harvest_rate=1/6, build_rate=1/3)
        add_tags(self, ['Metal'])
