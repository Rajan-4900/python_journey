# write  a program that takes  names of 3 favorite foods from the user and stores them in a list. 
# then print the list and its length.

food1 = input("Food-1: ")
food2 = input("Food-2: ")
food3 = input("Food-3: ")

# 1st Method to do 
food_list = [food1, food2, food3]
print("List Of the foods: ", food_list)
print("length of the list: ", len(food_list))
print("index 1: ", food_list[1])

print()
# 2nd Method
foodList = []
foodList.append(food1)
foodList.append(food2)
foodList.append(food3)

print("Lst Of Food: ", foodList)
print("Length Of the food: ", len(foodList))