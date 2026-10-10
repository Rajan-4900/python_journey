# Variable Local Vs Global
# Local Variable: A variable that is defined inside a function and can only be accessed within that function.
# Global Variable: A variable that is defined outside of any function and can be accessed from anywhere in the code.

# Local Variable Example:

def my_localvar():
    a = 5
    b = 10
    sum = a + b
    print(sum)  

my_localvar()       # Output = 15  
print(sum)          # Sum Is an Local Varibale we can't call the sum outside the function.

# Global Variable Example:
x = 10  # Global Variable 
def show():
    x = 5   # Local Variable
    print("Iside Funtion:", x)
show()
print("Outside Function: ", x)  # Output: Outside Function: 10
# we can call this x = 10 variable at any place in the code because it is a global variable.