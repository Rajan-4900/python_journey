# write a program that takes your favorite food name as input and print :
        # the middle 3 charactors
        # the last 2 charactors

fav_food = "ChickenBiryani"

# Index String : C h i c k e n B i r y  a  n  i
# +index Value : 0 1 2 3 4 5 6 7 8 9 10 11 12 13 

# printing middle 3 charactors
str_middle = fav_food[6:9]      # nBi
print("Middle 3 Char: ", str_middle)

# the last 2 charactors
str_last_char = fav_food[12:]        # ni
print("last 2 Char: ", str_last_char)

print()

# -ve Index Printing
# Index String :  C   h   i   c   k   e  n  B  i  r  y  a  n  i
# -index Value : -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# middle 3 char
neg_middle = fav_food[-9:-6]        # enB
print("Neg Middle Char: ", neg_middle)

# last 2 char
neg_last_char = fav_food[-2:]       # ni
print("Neg_Last2 Char: ", neg_last_char)
