#  Static Method Question 

# 1Q. Create a Static Method to valuate if a number is even.

class evennum:
    @staticmethod
    def even(num):
        if num % 2 == 0:        # Even Num Formula to find
            print("The Number Is Even ", num)
        else:
            print("The Number Is Odd ",num)

evennum.even(3)     # without the obj creation we can directly acces the function inside the class in this method