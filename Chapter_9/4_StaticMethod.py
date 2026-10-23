#  Static Method do not use self.
# They are used for utility-level function

# Example :
class Student:
    @staticmethod
    def classes():
        print("ABC College")

# Creating Object
s1=Student()    # Accesing the Class with New Obj
s1.classes()    # Calling the function with Obj

Student.classes()       # We can directly call the function without object