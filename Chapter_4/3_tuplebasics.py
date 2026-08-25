# Tuple Basics

myTuple = (23, 76, 87, 43, 54, 67, 54)
std_tuple = ("raj", "tuple", "laptop", "raj")


# std_tuple[1] = "raj"
print(std_tuple[2])

print(type(std_tuple))
print()

# Single tuple
std_single_tuple = (1)      # this will print integer
single_tuple = (1,)      # this will print Single Tuple ","
print("Single Value But Not Tupe: ",type(std_single_tuple))
print("Single Tuple With ',': ",type(single_tuple))

print()
# Empty Tuple
emptyTuple = ()             # Empty Tuple
print(type(emptyTuple))     # Checking the type of the tuple variable

print()

print(std_tuple.index("raj"))
print(std_tuple.count("raj"))