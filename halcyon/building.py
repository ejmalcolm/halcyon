from tags import add_tags, get_stat

class Building_Plan():

    def __init__(self, name, on_planet, in_octant, tags, player=0):
        self.name = name
        self.player = player
        self.planet = on_planet
        self.octant = in_octant
        #add the building plan to the contents of the octant
        self.octant.add_occupant(self)
        #initialize the default, blank values for each tag category
        self.tags = {'Material' : [], 'Structure' : [], 'Function' : []}
        #send the tag argument to the add_tags function
        add_tags(self, tags)
        #initalize the amount of Work needed to complete
        self.work_needed = get_stat(self, 'Work')

    def work_on(self, amount):
        self.work_needed -= amount
        if self.work_needed == 0:
            #plan_finished(self)
            print('A %s on %s, in %s, was finished.' %(self.name, self.planet, self.octant))
        else:
            print('%d units of Work left until %s is completed' % (self.work_needed, self.name))

    def __str__(self):
        return 'a building plan for a %s' % self.name
