# Negative indexing in python is used to access the elements from the end of the list. 
# The last element of the list is accessed by using -1, the second last element is accessed by using -2, and so on.

# Example of negative indexing in python:

str = "GulabJamun"

# Index Str  :  G   u  l  a  b  J  a  m  u  n
# Index Value: -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


str_1st_half = str[:-5]     # Gulab     -5-1==> -6--> Gulab
trial_half = str[-10:]      # GulabJamun  -10 - 1 ==> -9<--->-1

print("str_1st_half: ", str_1st_half)
print("str_1st_half: ", trial_half)

print()

# Secong Half Printing
sec_half = str[-5:]       # Jamun
trial_Sechalf = str[:-5]  # Gulab

print("sec_half: ", sec_half)
print("trial_Sechalf: ", trial_Sechalf)