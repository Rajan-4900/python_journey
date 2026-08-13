# write a program that:
    # takes a sentence as input
    # Convert it to LowerCase
    # Replaces all space " " with underScore "_"
    # Print the new String

str = input("Enter A String: ")
print(str)

print("Lower Case Letter:",str.lower())  # Lower Case

replace = str.replace(" ","_")  # Replaing the spaces
print("Replaced Space: ", replace)

print("The Final New Str: ", replace)