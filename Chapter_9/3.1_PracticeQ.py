#  Methods Practice Question (function Inside the class)

# 1Q. Create Class Student that Takes 3 Marks and has a method Average().
class Student:
    def __init__(self, name, ListOfMarks):
        self.name = name
        self.ListOfMarks = ListOfMarks 

    def avg(self):
        sum = 0
        for eachValue in self.ListOfMarks:
            sum += eachValue        # sum = sum + eachvalue

        average = sum/3
        print("Average Is: ",round(average,2))      # round(value, decimal value) it will gives only 2 decimal value

# Create Object
s1 = Student("John", [40, 65, 80])
s1.avg()



# 2nd Method to find the average 
class Student1:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg(self):
        average = sum(self.marks)/len(self.marks)
        print(f"Average Is : {average:.2f}")

# Creating Object To access the Average Value
std1 = Student("Python", [73, 40, 90])
std1.avg()