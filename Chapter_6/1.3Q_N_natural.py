# 4Q. write a program that prints the sum of first n natural numbers,
# For example, if n = 5, the output should be 15 (1 + 2 + 3 + 4 + 5 = 15)

n = int(input("Enter a Number: "))
sum = 0

while n >= 1:
    sum += n
    n -= 1
    print("sum: ",sum ,"N: ",n)