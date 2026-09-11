# Set Basics
# it will not give duplicate values

food = {"pizza", "burger", "pasta", "salad", "pizza"}

print(type(food))
print(food)

# Add new food in set
food.add("panipuri")
print(food)

# remove food from set
food.remove("pizza")
print(food)

# Empty Sets
emptySet = set()
print(type(emptySet))

# Empties the Set
# food.clear()
print(food)

# Removes A Randome Element From The Set 
# food.pop()
print(food)

# Combining Bothe Sets in one set (union)
charts = {"PaniPuri", "MasalaPuri", "BhelPuri", "DahiPuri"}
foody = food.union(charts)
print(foody)

# Common Elements Of bothe sets (intersection)

common = food.intersection(charts)
print(common)       # this will give empty set because there is no common element in both sets

charts.add("burger")
print(charts)
common = food.intersection(charts)
print(common)    # this will give common element in both sets