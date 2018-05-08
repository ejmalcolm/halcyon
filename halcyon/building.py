from object import Object
from tags import add_tags, get_stat, get_all_tags

class Building_Plan(Object):

    def __init__(self, name, on_planet, in_octant, tags, player=0):
        super().__init__(name, on_planet, in_octant, tags, player)
        #initalize the amount of Work needed to complete
        self.work_needed = get_stat(self, 'Work')

    def __str__(self):
        return 'a building plan for a %s' % self.name

    def work_on(self, amount):
        self.work_needed -= amount
        if self.work_needed == 0:
            #self.plan_finished()
            print('A %s on %s, in %s, was finished.' %(self.name, self.planet, self.octant))
        else:
            print('%d units of Work left until %s is completed' % (self.work_needed, self.name))

    def plan_finished(self):
        #create a Building() object and throw it the octant contents
        #this can repeat because variable names are just pointers
        #not overwriting the class every time, it still exists
        Building(self.name, self.planet, self.octant, get_all_tags(self), self.player)
        #remove the Building_Plan object from the octant
        self.octant.contents.remove(self)


class Building(Object):

    def __init__(self, name, on_planet, in_octant, tags, player=0):
        super().__init__(name, on_planet, in_octant, tags, player)
