# 1. Ask the User for their 3 favorite movie and store them in a list
# 2. Create a  tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min()
# 3. write  a program to ckeck grade based on marks (A/B/C/D) using if-elif-else.

# Q1 :

user1 = input("Enter 1st Movie: ")
user2 = input("Enter 2st Movie: ")
user3 = input("Enter 3st Movie: ")

fav_Movie = [user1, user2, user3]
print("List Of Users Fav Movies: ", fav_Movie)

print()
print()

# Q2 :

marks = (87, 64, 33, 95, 76)
print("Highest Marks In The Tuple: ", max(marks))
print("Lowest Marks In The Tuple: ", min(marks))

print()
print()

# Q3 :

std = int(input("Enter Your Marks: "))
if std > 85:
    print("Grade A")
elif std >= 70 <= 85 :
    print("Grade B")
elif std >= 50 <= 70 :
    print("Grade C")
else :
    print("Grade D")