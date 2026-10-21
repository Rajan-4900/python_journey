# File Handling Basics

# Reading a file by opening method and r method  r--->read by default it will be in read method
file = open("demofile.txt", "r")        # Open the file in read mode
data = file.read()                      # Read the contents of the file
print(data)

print()

# Writing the file in the writing mode
wrtfile = open("writefile.txt", "w")         # if the file is not created a manually then using this write mode it will automatically creates in the file
wrtfile.write("this is the 2nd example message for the write mode")         # this message will rewrite the exisiting message it will not go in new line 

print()

# appending the file using append method --> it will write the new messages and it will not rewrite the message in the exisiting message like write method

appfile = open("append.txt", "a")       # this will append the file by writing new message 
appfile.write("\n this is the printing message example in the terminal ")


# x letter will create a new file or it will give an error if exist in the file 
xfile = open("demofile.txt", "x")
xfile.write("this is the x file which it will analyse this file will exist or not")

# error if we run this code :
# Traceback (most recent call last):
#   File "d:\Coding\Python\Chapter_8\1.0_fileBasics.py", line 23, in <module>
#     xfile = open("demofile.txt", "x")
# FileExistsError: [Errno 17] File exists: 'demofile.txt'