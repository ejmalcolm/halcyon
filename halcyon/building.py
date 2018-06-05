from object import Object
from tags import add_tags

class BuildingPlan(Object):

    def __init__(self, name, on_planet, in_octant, tags, player):
        super().__init__(name, on_planet, in_octant, player)
        #initalize the amount of Work needed to complete
        self.work_needed = self.get_stat('Work')
        #add the tags
        add_tags(self, tags)
        #define what resource/s is needed to build the plan
        self.resource_needed = self.tags['Material']

    def __str__(self):
        return 'building plan for a %s' % self.name

    def work_on(self, amount):
        self.work_needed -= amount
        if self.work_needed <= 0:
            self.plan_finished()
            print('A %s on %s, in %s, was finished.' %(self.name, self.planet, self.octant))
        else:
            print('%d units of Work left until %s is completed' % (self.work_needed, self.name))

    def plan_finished(self):
        #remove the BuildingPlan object from the octant
        self.octant.contents.remove(self)
        #create a Building() object and throw it the octant contents
        #this can repeat because variable names are just pointers
        #not overwriting the class every time, it still exists
        created_building = Building(self.name, self.planet, self.octant, self.get_all_tags(), self.player)
        return created_building

class Building(Object):

    def __init__(self, name, on_planet, in_octant, tags, player):
        super().__init__(name, on_planet, in_octant, player)
        add_tags(self, tags)

    def __str__(self):
        return self.name
