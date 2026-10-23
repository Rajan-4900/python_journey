# Class And Object questions

# 1Q. Create a Class Car with attribute brand = "Scorpio".
class car:
    brand = "Scorpio"           # Attribute

# Creating Object for Accesing the car Class
Car = car()
print(Car.brand)

print()

# 2Q. Create a Class Laptop with attribute : brand , RAM, Price, Create 2 Objects with different values.
class laptop:
    brand = "Dell"
    ram = "128GB CAMM2 RAM"
    price = "₹7,99,990"

# Creating 2 Object to Access Class Attributes with different Value
Lap1 = laptop()
Lap1.brand = "HP"
Lap1.price = "₹1,99,990"
print(Lap1.brand)
print(Lap1.price)

print() 

Lap2 = laptop()
print(Lap2.brand)
print(Lap2.ram)