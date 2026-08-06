# arithmetic operators
x = 10
y = 5
print("Sum :", x + y)
print("Diff :", x - y)
print("Product :", x * y)
print("Division :", x / y)
print("Modulus :", x % y)
print("Exponent :", x ** y)

print()

# Comparison operators
print("Equal :", x == y)
print("Greater than :", x > y)
print("Less than :", x < y)
print("Greater than or equal :", x >= y)
print("Less than or equal :", x <= y)
print("Not equal :", x != y)

print()

# Logical Operators
# and  ---> if both the conditions are true then it will return true otherwise false
# # or  --> if any one of the condition is true then it will return true otherwise false
# # not --> it will return the opposite of the condition

print(x > y and x < y) #False
print(x > y or x < y)  #True
print(not(x > y))      #False

# Assignment Operators
a = 10
b = 10

# a = a + 5

# a += 5
# a -= 1
# a /= 2
# a *= 3
a += 5   # 15

print(a)   