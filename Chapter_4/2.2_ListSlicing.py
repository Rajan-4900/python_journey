# List slicing Python Program

# indexing

marks = [43, 65 ,32, 87 , 83, 21, 90]

print(marks[1])     # direct accesing the index values

# modified marks
marks[0]= 100
print(marks)        # 100, 65..............

# List Slicing
print(marks[1:3])       # [65, 32]

middle_index = len(marks)//2
output = marks[middle_index-1:middle_index+2]

print(output)           # [32, 87, 83]

print(marks[-1:])       # [90]
print(marks[:-1])       # [100, 65 ,32, 87 , 83, 21] with modified value