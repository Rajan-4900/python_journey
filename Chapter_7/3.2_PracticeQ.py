# 1Q. write a function show_age(name, age) that prints: "Rajan L is 21 year old"

def show_age(name, age):
    print(f"{name} is {age} year old")

show_age("rajan", 21)

# 2Q. create a function add_numbers(a,b) that prints the sum and difference
def add_numbers(a,b):
    sum1 = a + b
    diff = a-b
    print(f"Sum is {sum1} and the Difference is {diff}")

add_numbers(10, 5)
add_numbers(23, 67)
add_numbers(45, 56)

# 3Q. write function fav_food(food) that prints "luffy loves <food-meat>
def fav_food(food):
    print("luffy loves ", food)

fav_food("meat")
fav_food("meat grilld")
