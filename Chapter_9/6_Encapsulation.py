# Oops Concept :
# in this opps concept there are 4 pillars :
# 1. Abstraction
# 2. Encapculation
# 3. Inheritance
# 4. PolyMorphism

# Encapsulation : - wrapping data + methods inside a single unit (calss)
#  data is protected using private variable

# Example Code :
class Account:
    def __init__(self, bal):
        self.__balance = bal        # Private

    def show_balance(self):
        print("Balance: ",self.__balance)

# obj
acc1 = Account(50)
acc1.show_balance()