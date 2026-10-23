#  Build Account Class
# task :
# create an Account class with :
#     * Attributes    -> balance, account number
#     * Methods       -> debit, credit, print balance

class Account :
    def __init__(self, accNum, balance):
        self.accNum = accNum
        self.balance = balance

    def credit(self, amount):
        self.balance += amount
        print("Amount Credited: ", amount)

    def totalBal(self):
        print("Total Balance: ", self.balance)

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount debited: -", amount)
        else:
            print("Insufficient Balance")
    def show_balance(self):
        print(f"Account: {self.accNum}, Balance: {self.balance} ")

# obj creation
acc = Account("123456789", 50000)
acc.credit(20000)
acc.totalBal()
acc.debit(10000)
acc.show_balance()

