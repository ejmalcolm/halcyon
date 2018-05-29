from collections import Counter

class Player():

    instances = []

    def __init__(self, name, slaved=False):
        #add self to instances for gamestate purposes
        self.__class__.instances.append(self)
        self.name = name
        #if applicable, the player who has control over this player's actions
        self.slaved = slaved
        #the resources that this player has access to
        self.resources = []
        self.client_methods = (
                                ('Display resources', self.get_resources, None, False),
                                ('Display description', self.__str__, None, False)
        )

    def __str__(self):
        return '%s' % self.name

    def gain_resource(self, resource, amount=1):
        for _ in range(amount):
            self.resources.append(resource)

    def get_resources(self):
        counted_resources = Counter(self.resources)
        returnstring = ''
        for count in counted_resources:
            returnstring += '%s: %s<br>' % (count, counted_resources[count])
        return returnstring

GM = Player('Gamemaster')
