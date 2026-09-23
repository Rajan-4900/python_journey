# After chapter 6 

# Question / Problem Statement: Create a console-based Expense Tracker program in Python that allows the user 
# to record daily expenses and view summaries like total spending. Use only the concepts learned till Chapter 6
# (loops, conditionals, lists, dictionaries, and basic input/output).

# Project Details / Description:
# You are required to build a simple personal finance management tool.
# The program should allow the user to:
#   ● Add an expense with details like date, category, description, and amount.
#   ● View all recorded expenses in a clean format.
#   ● Calculate total spending so far.
#   ● Exit the program gracefully when the user chooses to.
# All tasks must be implemented using loops, if-else, lists, and dictionaries
# only. No user-defined functions or file handling should be used.


# Expense Tracker Project

expensesList = []    # storing all expenses in form of dictionary 

print("Welcome To Expense Tracker")

while True :
    print("\n======MENU======")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Expense")
    print("4. Exit\n")

    choice = int(input("Please Enter Your Choice : "))

# ADD EXPENSE
    if (choice == 1):
        date = input("Enter Your Date: ")
        cateogry = input("Enter Expense Category: ")
        description = input("Enter Your Expense Description: ")
        amount = float(input("Enter Your Expense Ammout: "))

        # Creating Dictionary Using Above Statement
        expense = {
            "Date" : date,
            "Category" : cateogry,
            "Description" : description,
            "Amount" : amount
        }

        expensesList.append(expense)    # Adding this above dictionary to the expenses List in the 20th line code
        print("Expenses Added Succesfully\n ")

# VIEW ALL EXPENSES
    elif (choice == 2):
        if not expensesList:
            print("No expenses Added\n")
        else:
            print("\n===This Your Expenses===")
            count = 1

            for eachExpense in expensesList :
                print(f"Expense Number {count} -> {eachExpense["Date"]}, {eachExpense["Category"]}, {eachExpense["Description"]}, {eachExpense["Amount"]},")
                count += 1

# VIEW TOTAL EXPENSES
    elif (choice == 3):
        total = 0
        for eachExpenses in expensesList:
            total = total + eachExpenses["Amount"]

        print("Total Expense Is :", total)

#  Exit
    elif(choice == 4):
        print("Thank You For Using Our System \n")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN\n")

