import json

class bit(object):
    def __init__(self, bitID):
        self.bitID = bitID
        self.energy = 100
        self.cycles = 0
        self.task = "NULL"
    
    def get_data(self):
        data =  { 
            "energy": self.energy, 
            "cycles": self.cycles,
            "task": self.task
        }
        return json.dumps(data)
    
    def set_task(self, task):
        self.task = task

    def cycle(self):
        c = self.cycles
        c = c + 1
        self.cycles = c
