# 1. 
#     a. duck typing is a concept in programming where the type or class of an object is determined by its behavior rather than its explicit inheritance from a specific class. In other words, if an object behaves like a certain type, it can be treated as that type, regardless of its actual class.
#     b. The car needed a speak attribute in order for it to work in the same loop sa the other objects

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on the water.")

class Drone:
    def move(self):
        print("The drone flies in the air.")

def start_transportation(vehicle):
    vehicle.move()

car1 = Car()
boat1 = Boat()
drone1 = Drone()

vehicles = [car1, boat1, drone1]

for vehicle in vehicles:
    start_transportation(vehicle)