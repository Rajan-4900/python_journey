# File Handling Basics

# Reading a file by opening method and r method  r--->read by default it will be in read method
file = open("demofile.txt", "r")        # Open the file in read mode
data = file.read()                      # Read the contents of the file
print(data)