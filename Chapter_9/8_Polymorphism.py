# Oops Concept :
# in this opps concept there are 4 pillars :
# 1. Abstraction
# 2. Encapculation
# 3. Inheritance
# 4. PolyMorphism

# Polymorphism :- Same function name, but different behaviour in different Classes ,
# one function name -> many different behaviours depending on the object calling it.
# Think
    # different obj respond in their own unique way

# if i say Sound
    # a dog will Bark 
    # a cat wil meow
    # a cow will moo

# Example Code : Animal Sound
class dog():
    def sound(self):
        print("Dog Say: Bark")

class cat():
    def sound(self):
        print("Cat Say: Meow")

class cow():
    def sound(self):
        print("Cow Say: Mooo")

# Polymorphism in Action
animals = [dog(), cat(), cow()]
for a in animals:
    a.sound()

# Or we can Access the class In Normal Way : 

# Creating Object
# Dog = dog()
# Cat = cat()
# Cow = cow()

# Dog.sound()
# Cat.sound()
# Cow.sound()