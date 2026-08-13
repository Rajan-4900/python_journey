# write  a program that takes a sentence as input and print:
    # Total characters(len())
    # UpperCase Version 
    # LowerCase Version
    # Add Some Emoji In Between

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

