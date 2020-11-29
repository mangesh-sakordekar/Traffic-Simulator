'''
    file Street.py
    This file holds the class Street.
'''
from sakordekar_mangesh.Block import *
from sakordekar_mangesh.Light import *


'''
    class Street
    class Car holds the details of the whole street in the traffic simulator.
    It holds the blocks and counts for blocks, lights and cars.
'''


class Street:

    road = []
    car_count = 0
    num_blocks = 1
    num_lights = 0

    '''
        __init__(self)
        This function initializes all the variables of the class Street
        and adds the first block to the street.
        self - holds the current class
    '''
    def __init__(self):
        self.road = []
        self.num_blocks = 1
        self.num_lights = 0
        self.car_count = 0
        b = Block(0.5, 30, 0)
        self.road.append(b)

    '''
        def addBlock(self)
        This function adds a block and light to the street.
        It prompts the user to input block details.
        self - holds the current class
    '''
    def addBlock(self):

        #Inputs for light
        while True:
            try:
                cycle = input("Length of cycle: ")
                while float(cycle) <= 0:
                    cycle = input("Invalid Input. Try again.\nLength of cycle: ")
                break

            except:
                print('Invalid input. Try again.')

        l_temp = Light(cycle)
        self.road.append(l_temp)
        self.num_lights += 1

        #inputs for the block
        while True:
            try:
                length = input("Length of Block in miles: ")
                while float(length) <= 0.5:
                    length = input("Invalid Input. Try again.\nLength of Block in miles: ")
                break

            except:
                print('Invalid input. Try again.')

        while True:
            try:
                max_speed = input("Speed limit of block in mph: ")
                while float(max_speed) <= 0:
                    max_speed = input("Invalid Input. Try again.\nSpeed limit of block in mph: ")
                break

            except:
                print('Invalid input. Try again.')

        b = Block(length, max_speed, self.num_blocks)
        self.road.append(b)
        self.num_blocks += 1



    '''
        printRoads(self)
        This function uses the iterator pattern to go 
        through each block and light. For a block, it
        prints the number of cars in each lane and for light 
        it prints if the light is on or not.
        self - holds the current class
    '''
    def printRoads(self):

        print("Entry/Exit")
        for i, v in enumerate(self.road):
            v.printObj()
        print("Entry/Exit")

    '''
        selectEnd(self)
        Prompts the user to input the end at which the 
        car should be added and calls functions to add 
        a new car on the street. 
        self - holds the current class
    '''
    def selectEnd(self):

        ind = input('Which end: 0) top 1) bottom: ')
        self.car_count += 1
        while True:
            if ind == '0':
                self.road[0].addNewCar("down", self.car_count)
                break
            elif ind == '1':
                self.road[self.num_blocks+self.num_lights-1].addNewCar("up", self.car_count)
                break
            else:
                ind = input('Invalid input. Try again.\nWhich end: 0) top 1) bottom: ')

    '''
        showCars(self)
        Uses iterator pattern to display location 
        of cars in each block. 
        self - holds the current class
    '''
    def showCars(self):

        print('In showCars')
        for i, v in enumerate(self.road):
            v.displayCars()

    '''
        updateStreet(self)
        Uses iterator pattern to update each block and light by 30 seconds 
        self - holds the current class
    '''
    def updateStreet(self):
        for i, v in enumerate(self.road):
            v.updateTime()

        count = 0
        temp = Block()
        while count < len(self.road):
            if count == len(self.road)-1:
                self.road[count].updateCarsDown(True,temp)
            else:
                self.road[count].updateCarsDown(self.road[count+1].getLight(), self.road[count+2])
            count += 2

        count = 0
        while count < len(self.road):
            if count == 0:
                self.road[count].updateCarsUp(True, temp)
            else:
                self.road[count].updateCarsUp(self.road[count-1].getLight(), self.road[count-2])
            count += 2
