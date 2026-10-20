# practice questio for readin a file by opening method

# 1Q. write a code to open a file named as mydata.txt in read mode.
file = open("mydata.txt")       # by default it will be in read mode without adding "r"
data = file.read()
print(data)

print()
# 2Q. Write a program to read a text from a given file certificate.txt and find whether it contains the word live.
givenfile = open("certificate.txt") 
givdata = givenfile.read()
print(givdata)

givdata = givdata.lower()       # it will make all upper case letter to lower case letter

# checking with if condition
if "live" in givdata :
    count = givdata.count("live")           # counting the number of same words
    print("Yes Live word is there", count, "times")
else:
    print("No Its not there")