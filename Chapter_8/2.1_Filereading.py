# this file is for only reading mode 
file = open("demofile.txt")
data = file.read()
print(data)
file.close()                    # we should close this reading method file otherwise it will consume more memory

print()
# or 
# we have another method 

# using "with" keyword it will automatically close the file example:

# a. read entire file : 
with open("notes.txt", "r") as f:
    data = f.read()
    print("with keyword file: ", data)

# b. read line by line :
with open("notes.txt", "r") as a:
    line1 = a.readline()        # this we have to do for all line to read by reading line by line
    line2 = a.readline()
    line3 = a.readline()
    print("Reading Line By Line: ", line3)

# c. read all lines :
with open("notes.txt", "r") as b:
    lines = b.readlines()
    print("reading Lines: ", lines)


# For writing file also same keyword 
with open("witefile.txt", "w") as c:
    c.write("\n this is the new message from the new write function using with keyword ")

# For Append Also Smae method using with keyword
with open("append.txt", "a") as d:
    d.write("\n\n this is the new append method using with keyword ")