# Create a Dictionary named marks to store marks of 3 subjects.
# add the subjects one  by one and print final dictionary.

# Example
# Input :
# Maths -> 90
# Science -> 85
# English -> 88

# Output : 
# {'Maths':90, 'Science':85, 'English': 88}

marks = {
    input("Enter subject name 1: ") : int(input("Enter marks: ")),
    input("Enter Subject Name 2: ") : int(input("Enter Marks: ")),
    input("Enter Subject Name 3: ") : int(input("Enter Marks: "))
}

print(marks)

marks["Social"] = 89
print(marks)
