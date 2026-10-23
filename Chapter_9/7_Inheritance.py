# Oops Concept :
# in this opps concept there are 4 pillars :
# 1. Abstraction
# 2. Encapculation
# 3. Inheritance
# 4. PolyMorphism

# Inheritance :- when one class (child) gets properties and methods of another class (parent) it avoids
# repeating code
# Think :
    # child class uses everithing the parent class already has.

# Example Code :
class Vehicle:
    def start(self):
        print("Vehicle is Starting")

class car(Vehicle):
    def drive(self):
        print("Car Is now Moving")

class bike(Vehicle):
    def ride(self):
        print("Bike Is now riding")

class truck(Vehicle):
    def load(self):
        print("Truck Is now Loading")

# Creating Obj To Call parent and Child Classes
v = Vehicle()
v.start()           # Parent obj Calling

print()

C = car()
C.start()           # from parent class
C.drive()           # Child of Car

print()

B = bike()
B.start()           # from parent class
B.ride()            # child class of Bike

print()

T = truck()
T.start()           # from parent class
T.load()            # Child Class Of Truck