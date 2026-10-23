#  Methods (Function Inside the Class) 

# Example : 
class Student:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Hello", self.name)

# Creating an Object 
s1 = Student("Python")
s1.hello()