# Function Parameter
# Function can Accept parameters, data passed from outside. 
# the value given when calling the function are arguments.

# Function Defination with parameter (a, b)
def avg(a, b):
    avgVal = (a+b)/2
    print("the avg value is: ", avgVal)

# Function Calling with Arguments function(argument)
avg(5, 8)
avg(2, 7)
avg(3, 6)
avg(24, 67)

print()

def paraName(name):
    print("Hello", name)

paraName("Rajan")
paraName("Python")

print()

def Sum(a,b):
    val = a + b
    print(val)

Sum(5,10)
Sum(48,23)
Sum(50,100)