from lib_bitsen.bitsen import bit
from lib_bitsen.cycle import cycle
import time
import random

class simulate(object):
    def __init__(self, cyclespeed):
        self.cyclespeed = cyclespeed
        self.cycles = 0

    def simulate(self):
        while(True):
            time.sleep(self.cyclespeed)
            print(self.cycles)
            self.cycles = self.cycles + 1


    def defaultstart(self):
        
        bits = [bit() for i in range(10)]
        for bit in bits:
            print(bit.get_data())

            