
from sakordekar_mangesh.Street import *


class Simulator:

    street_road = Street()

    def __init__(self):

        while True:
            print('0) show road\n1) update\n2) add car\n3) add block\n4) show cars\n5) quit\n')
            cmd = input("Choice: ")
            if cmd == '0':
                self.street_road.printRoads()
            elif cmd == '1':
                self.street_road.updateStreet()
                self.street_road.printRoads()
            elif cmd == '2':
                self.street_road.selectEnd()
            elif cmd == '3':
                self.street_road.addBlock()
            elif cmd == '4':
                self.street_road.showCars()
            elif cmd == '5':
                break
            else:
                print('Invalid choice, please try again!')
