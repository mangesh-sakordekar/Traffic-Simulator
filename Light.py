'''
    file Light.py
    This file holds the class Light.
'''

'''
    class Light
    class Car holds the details of each light in the traffic simulator.
    It holds the cycle time and if the light is on or off.
'''


class Light:

    cycle = 0
    time_passed = 0
    is_on = False

    def __init__(self, cyc=1):

        self.time_passed = 0
        self.cycle = float(cyc)

    def printObj(self):

        if self.is_on:
            print('On')
        else:
            print('Off')

    def displayCars(self):
        pass

    def getLight(self):
        return self.is_on

    def updateTime(self):
        self.time_passed += 30
        if self.time_passed/60 >= self.cycle:
            self.time_passed = 0
            self.is_on = not self.is_on
