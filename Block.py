'''
    file Block.py
    This file holds the class Block.
'''
from sakordekar_mangesh.Car import *


'''
    class Block
    class Car holds the details of each Block in the traffic simulator.
    It holds the length of the block, max speed, car counts, cas and block id.
'''


class Block:

    block_length = 0.5
    max_speed = 30.0
    car_up_count = 0
    car_down_count = 0
    block_id = -1
    cars_up = []
    cars_down = []

    '''
        __init__(self, length=0.5, speed=30, b_id=0)
        This function initializes all the variables of the class Block.
        self - the current class
        length - holds the length of the block in miles
        speed - holds the max speed of the block
        b_id - holds the block id
    '''
    def __init__(self, length=0.5, speed=30, b_id=-1):

        self.block_length = float(length)
        self.max_speed = float(speed)
        self.block_id = int(b_id)
        self.car_up_count = 0
        self.car_down_count = 0
        self.cars_up = []
        self.cars_down = []

    def printObj(self):

        print("up: " + str(self.car_up_count) + " down: " + str(self.car_down_count))

    '''
        addNewCar(self, direction='down', car_id=-1)
        Adds a new car to the block and updates the counts.
        self - holds the current class
        direction - holds the direction of the car
        car_id - holds the car id
    '''
    def addNewCar(self, direction='down', car_id=-1):
        car = Car(direction, self.max_speed, car_id, self.block_length)
        if direction == 'down':
            self.car_down_count += 1
            self.cars_down.append(car)
        else:
            self.car_up_count += 1
            self.cars_up.append(car)
        return

    '''
        displayCars(self)
        Uses the iterator pattern to display the id and 
        location of each car in the block
        self - holds the current class
    '''
    def displayCars(self):
        print("Block " + str(self.block_id) + "-------------------")
        print("Up----")
        for i, v in enumerate(self.cars_up):
            v.printIdLoc()
        print("Down---")
        for i, v in enumerate(self.cars_down):
            v.printIdLoc()

    def getLight(self):
        return True

    def getSpeed(self):
        return self.max_speed

    def getLength(self):
        return self.block_length

    def appendCarUp(self, car):
        self.cars_up.append(car)
        self.car_up_count += 1

    def appendCarDown(self, car):
        self.cars_down.append(car)
        self.car_down_count += 1

    def updateTime(self):

        for i, v in enumerate(self.cars_down):
            v.updateCar()
        for i, v in enumerate(self.cars_up):
            v.updateCar()

    def updateCarsDown(self, downLight, nextBlock):
        count = 0
        while count < len(self.cars_down):
            if self.cars_down[count].getLocation() > self.block_length:
                if downLight:
                    self.cars_down[count].setNewBlock(0, nextBlock.getSpeed())
                    nextBlock.appendCarDown(self.cars_down[count])
                    self.cars_down.remove(self.cars_down[count])
                    self.car_down_count -= 1

                else:
                    self.cars_down[count].setNewBlock(self.block_length, self.max_speed)
                    count += 1

            else:
                count += 1

    def updateCarsUp(self, upLight, nextBlock):
        count = 0
        while count < len(self.cars_up):
            if self.cars_up[count].getLocation() <= 0:
                if upLight:
                    self.cars_up[count].setNewBlock(nextBlock.getLength(), nextBlock.getSpeed())
                    nextBlock.appendCarUp(self.cars_up[count])
                    self.cars_up.remove(self.cars_up[count])
                    self.car_up_count -= 1

                else:
                    self.cars_up[count].setNewBlock(0, self.max_speed)
                    count += 1

            else:
                count += 1
