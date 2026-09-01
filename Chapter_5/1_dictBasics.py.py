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

# Removing the Item
student.pop("College")
print(student)

# Return All Keys
print(student.keys())  # dict_keys(['name', 'Age', 'City', 'Goal'])

# return All Values
print(student.values()) # dict_values(['Rajan', 21, 'Hyderabad', 'Software Engineer'])

# return all key-vlaue pairs as tuples
print(student.items())  # dict_items([('name', 'Rajan'), ('Age', 21), ('City', 'Hyderabad'), ('Goal', 'Software Engineer')])

# return value of a key safely
print(student.get("name"))      #Rajan

# Updates Dictionary with another dictionary
student.update({"Age": 22, "City": "Chennai"})      
print(student)  # {'name': 'Rajan', 'Age': 22, 'City': 'Chennai', 'Goal': 'Software Engineer'}