
class cycle(object):
    def __init__(self):
        self.cycles = 0

    def cycle(self):
        print("Cycles: " + str(self.cycles))
        self.cycles = self.cycles + 1