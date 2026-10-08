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

# Defaut=lt Function if we do not pass any value to the function then it will take the default value.
def defaultpara(a=5, b=10):         # default function parameter created ex: a=5, b=10
    sum = a+b
    print("The Sum Is: ",sum)

# Function calling with parameter
defaultpara(50, 100)
defaultpara(23, 10)
defaultpara()           # we are not pasing any value in this so thats y it is a Defualt Value function call and it will not print at the end

