# Q1: write  a program that takes a sentence as input and print:
    # Total characters(len())
    # UpperCase Version 
    # LowerCase Version
    # Add Some Emoji In Between

# Q2: write a python program that takes any word or sentence as input and print:
    # the 1st character
    # the last character
    # total Number of character

# Q1
ass = input("Enter A Sentence: ")

ass = ass.replace(":)", "🙂")
ass = ass.replace(":(", "😔")
ass = ass.replace(":D", "😀")
ass = ass.replace(";)", "😉")
ass = ass.replace(":}", "😍")

print("Final Str : ",ass)
print("Length Of the Sentence: ", len(ass))
print("Upper Case: ", ass.upper())
print("Lower Case: ", ass.lower())

print()
# Q2

user = input("Enter the sentence: ")

split = user.split()
first_char = split[0]
mid_char = len(split)//2
mid = split[mid_char]
last_char = split[-1]

print("Splited Char: ",split)
print("1st Char: ",first_char)
print("Mid Char: ", mid_char)
print("last Char: ",last_char)
print("Length Befor Update: ",len(user))
print("Length After Update: ",len(split))