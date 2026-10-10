# 1Q. Write a program with a local variable score inside a function and global one outside
scope = "Global Scope"      # Global Variable
def my_Scope():
    scope = "Local Scope"         # Local Variable
    print("Inside the function: ", scope)    # Output: Inside the function: Local Scope

my_Scope()
print("outside the function scope: ", scope)    # Output: outside the function scope: Global Scope

print()

# 2Q. Create a program using global keyword to modify a variable from inside  a function


# 3Q. Explain the different between Local and Global scope in your  own words with an example