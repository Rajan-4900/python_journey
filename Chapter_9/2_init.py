# __init__() function runs automatically whenever an object is created it is used to initialize attributes. 

#  Example :
class Student:
    college = "XYZ College"

    def __init__(self, name):
        # print("This is called Automatically when Object is Accesing the class")
        # print(self)
        self.name = name


# Creating Object
std1 = Student("Rajan")        # this will automatically Calls the inti method
print(std1.college)
print("Self Example output: ", std1)             # self testing 
print(std1.name)

print()

std2 = Student("Python")
print(std2.name)