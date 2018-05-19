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


    def __str__(self):
        return 'player: %s' % self.name

    def gain_resource(self, resource, amount=1):
        for _ in range(amount):
            self.resources.append(resource)

GM = Player('gamemaster')
