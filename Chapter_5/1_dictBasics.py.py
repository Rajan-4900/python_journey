# Dictionary Basics

student = {
    "name" : "Rajan",
    "Age": 21,
    "City" : "Bangalore",
    "College" : "XYZ Clg"
}

print(type(student))  # <class 'dict'>
print(student["name"])      # Rajan

print(student)      # {'name': 'Rajan', 'Age': 21, 'City': 'Bangalore', 'College': 'XYZ Clg'}

# Updating the values
student["City"] = "Hyderabad"
print(student)

# Adding the new key-value pair
student["Goal"] = "Software Engineer"
print(student)

