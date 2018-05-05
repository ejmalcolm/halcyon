class ABC():

    def __init__(self):
        self.n = 1

class EFF(ABC):

    def __init__(self):
        super().__init__()

me = EFF()

print(me.n)
