class Player():

    def __init__(self, name, id_number, slaved=False):
        self.name = name
        self.id = id_number
        self.slaved = slaved

    def __str__(self):
        return 'player: %s' % self.name

    def gain_resource(self, resource, amount=1):
        pass
