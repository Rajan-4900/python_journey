# 1Q. Write a program with a local variable score inside a function and global one outside
scope = "Global Scope"      # Global Variable
def my_Scope():
    scope = "Local Scope"         # Local Variable
    print("Inside the function: ", scope)    # Output: Inside the function: Local Scope

my_Scope()
print("outside the function scope: ", scope)    # Output: outside the function scope: Global Scope

print()

# 2Q. Create a program using global keyword to modify a variable from inside  a function
x = 10      # Global Variable
def modifyvar():
    #global + modification of the global variable
    global x
    x = 50
    print(x)

# Calling the Function 
modifyvar()
print("Value of x after modification: ", x)    # Output: Value of x after modification: 50

print()
# 3Q. Explain the different between Local and Global scope in your  own words with an example
# Local Scope: A variable created inside a function. We can normally use it only inside that function.
# Global Scope: A variable created outside all functions. We can use it both inside and outside functions for reading, subject to Python's rules.

# Example: 

x = 10  # Global variable
def my_function():
    y = 20  # Local variable
    print("Global variable:", x)
    print("Local variable:", y)

my_function()
print("Outside function:", x)
# print(y)  # This would cause an error