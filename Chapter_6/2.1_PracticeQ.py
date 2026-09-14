# 1Q.write a program using for and range() to print all even number between 1 and 20 
for num in range(2, 21, 2):
    print(num)

print()

# 2Q. write a program to print number 1 to 50 but print "Rajan L" instead of numbers that are multiples of 5
# ex: Output: 1 2 3 4 Rajan 6 7 8 9 Rajan......
for num in range(1, 51):
    if num % 5 == 0:
        print("Rajan L")
    else:
        print(num)

print()

# 3Q. write a program to print the square of each number from 1 to 10 using a for loop 
# ex: 1 4 9 16 25 36 49 64 81 100
for i in range(1 , 11):
    print(i**2)

print()

# 4Q. write a program to print the multiplication table of any number entered by the user using a for loop 
t = int(input("Enter multiplication Table: "))
for j in range(1, 11):
    print(f"{t} x {j} = {t*j}")

print()

# 5Q. write a program that prints all numbers from 100 to 1 using for and range().
for k in range(10, 0, -1):
    print(k)

print()

# 6Q. rajan want to print his username five times in uppercase letters.
k = input("Enter Your User Name: ")
for user in range(1, 6):
    print(user, k.upper())

print()

# 7Q. you are given a list of rajan favorite foods. write a python program to print each food item using a for loop
favfoodlist = ["PaniPuri", "MasalPuri", "dahipuri", "aloo tikki"]
for item in favfoodlist:
    print(item)
print(type(favfoodlist))

print()

# 8Q. rajan has created a tuple of famouse temples where he wants to go in future. write a python program 
# to print each temples using a for loop
favplaceTuple = ("Ayodhya", "Kedarnath", "Jagannath Puri", "Vrindavan", "Dwarkadhish Temple")
for items in favplaceTuple:
    print(items)
print(type(favplaceTuple))
