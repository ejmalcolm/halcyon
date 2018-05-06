class Player():

    def __init__(self, name, id_number, slaved=False):
        self.name = name
        #single digit number used to identify the player
        self.id = id_number
        #if applicable, the player who has control over this player's actions
        self.slaved = slaved
        #the resources that this player has access to
        self.resources = []

    def __str__(self):
        return 'player: %s' % self.name

    def gain_resource(self, resource, amount=1):
        for _ in range(amount):
            self.resources.append(resource)
