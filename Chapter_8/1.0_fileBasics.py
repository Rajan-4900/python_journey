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
