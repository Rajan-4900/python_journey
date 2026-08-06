# write a program that takes two numbers and prints :
    # their sum, difference and Product
    # whether the first number is greater than the second number 

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd Number: "))

# printing the Sum, difference and product
print("Sum: ", x + y)
print("Diff: ", x - y)
print("Product: ", x * y)

# checking whether the first number is greater than the second number
if x > y :
    print("then 1st number is greater than 2nd number")
else :
    print("The 1st number is less than 2nd number")
