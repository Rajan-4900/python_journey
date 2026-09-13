# write a program to print the multiplication table of a any number using a while loop

num = int(input("enter a Number: "))
i = 1
while i <= 10:
	print(f"{num} x {i} = {num*i}")
	i += 1