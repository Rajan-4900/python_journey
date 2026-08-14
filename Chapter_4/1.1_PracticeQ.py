# write a python program that takes a number as input and print:
    # positive if number > 0
    # Zero if number == 0
    # Negetive if number < 0

num = int(input("Enter a Random Number: "))

if (num > 0):
    print("It's Positive Number")
elif(num < 0):
    print("It's A Negetive Number")
elif(num == 0):
    print("It's A Zero Number")
else:
    print("Nothing To Print")