# Lists Methods Python Programming

marks = [43, 65 ,32, 87 , 83, 21, 90]
print("Before the len: ", len(marks))
print(marks)

print()
# add the given list eliment at the end by selecting
marks.append(100)        
print(marks)            # [43, 65 ,32, 87 , 83, 21, 90, 100]
print("After the len: ", len(marks))

print()
# Insert element at index  [marks.insert(index,value)]
marks.insert(2,23)      # 32--->23 through index
print("Insert element at Index: ",marks)
print("After the len: ", len(marks))

print()
# List Element Remove
marks.remove(83)
print("List Eliment Remove Method: ", marks)        # 83 will be removed from the list
print("After the len: ", len(marks))

print()
# removing element at index
marks.pop(5)
print("removed the element through the index: ",marks)
print("After the len: ", len(marks))

print()
# List Sorting 
marks.sort()
print("List Sorting: ",marks)

print()
# reversing the element
print("Befor the reverse: ", marks)
marks.reverse()
print("After Reversed the values: ", marks)