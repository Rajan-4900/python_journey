#  class in oops is a blue print or a template

# Example :
# Creating a Class called Vehicale
class Vehicle:
    bike = "KTM Duke 200"                    # attributes
    engine = "199.5 cc liquid-cooled"              # attributes
    colour = "orange and black"     # attributes
    mileage = "35"                  # attributes

# Creating an Object 
Bike = Vehicle()
print("Bike Type: ",Bike.bike)            # accesing the class by object.AttributeName

Colour = Vehicle()
print("Car Colour: ", Colour.colour)

Engine = Vehicle()
print("Machine Type or Model: ", Engine.engine)

# we have created 1 class of the vehicle and 3 object of that class

