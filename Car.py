'''
    file Car.py
    This file holds the class car.
'''

'''
    class Car
    class Car holds the details of each car in the traffic simulator.
    It holds the direction, speed, location and id of each car.
'''


class Car:

    car_direction = 'down'
    car_type = 'normal'
    car_speed = 0
    car_id = -1
    car_location = 0

    def functionChoice(self):
        return

    '''
        __init__(self, direction='down', speed=0, c_id=-1, length=0)
        This function initializes all the variables of the class Car.
        self - the current class
        direction - holds the direction in which the car is moving
        speed - holds the max speed of the block
        c_id - holds the car id
        length - holds the length of the block
    '''
    def __init__(self, direction='down', speed=0, c_id=-1, length=0):
        #ALL instance variables should go here
        self.car_direction = direction
        self.car_id = int(c_id)
        self.car_speed = float(speed)
        if direction == 'down':
            self.car_location = 0
        else:
            self.car_location = float(length)
        self.setCarType()
        #self.assignCarType()

    def printCar(self):
        print("car id: " + str(self.car_id))

    def printIdLoc(self):
        print(str(self.car_id) + ": " + str(self.car_location))


    def setCarType(self):

        while True:
            choice = input('Which type: 0) slow 1) normal 2) fast: ')
            if choice == '0':
                self.nervousCar()
                self.car_type = 'slow'
                break
            elif choice == '1':
                self.normalCar()
                self.car_type = 'normal'
                break
            elif choice == '2':
                self.aggressiveCar()
                self.car_type = 'fast'
                break
            else:
                print('Invalid input. Try again.')

    '''
    def setChoice(self, funName):
        self.foo = funName

    def assignCarType(self):
        self.foo()
    '''

    def normalCar(self):
        self.car_speed -= 5

    def nervousCar(self):
        pass

    def aggressiveCar(self):
        self.car_speed += 5

    def updateCar(self):
        if self.car_direction == 'down':
            self.car_location += self.car_speed / 120
        else:
            self.car_location -= self.car_speed / 120

    def getLocation(self):
        return self.car_location

    def setNewBlock(self, location, speed):
        self.car_location = location
        if self.car_type == 'normal':
            self.car_speed = speed
        elif self.car_type == 'fast':
            self.car_speed = speed + 5
        elif self.car_type == 'slow':
            self.car_speed = speed - 5
