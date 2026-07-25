# Type Convertion 
# 1. Implicit Type Conversion    ----> Converts Automatically
# 2. Explicit Type Conversion    ----> Converts Manually (we have to do it)


#Implicit Type Conversion
x = 10  #int
y = 1.5  #float
z= x+y  # it converts int to float
print(z)

# Explicit Type Conversion
a = 10  #int
b = 1.5 #float
z = float(a) + b  # it converts int->a to float->a  10 ---> 10.0
print(z)