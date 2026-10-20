# practice questio for readin a file by opening method

# 1Q. write a code to open a file named as mydata.txt in read mode.
file = open("mydata.txt")       # by default it will be in read mode without adding "r"
data = file.read()
print(data) 