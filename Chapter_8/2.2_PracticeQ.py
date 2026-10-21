# practice question reading the file

# 1Q. read only the 1st line of demofile.txt
with open("demofile.txt", "r") as f:
    data = f.readline()
    print("1st line", data)

print()

# 2Q. Print how many lines are present in notes.txt
with open("notes.txt", "r") as a:
    ListOfLines = a.readlines()
    print("Read all Lines :", ListOfLines)
    print("Number of Lines in file: ", len(ListOfLines))        # it will count in the list by use of index      