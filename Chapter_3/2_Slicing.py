# Slicing The Given String    index_value-1  [start : end]--> index_value

str = "GulabJamun"
#      0123456789 -----> index values to understand in a better way

# 1st half of the string
first_half = str[0:5]   # Gulab     5-1==> 4--> gulab
trial_half = str[:6]    # GulabJ    6-1==> 5--> GulabJ

print("First_Half: ", first_half)
print("Trial_Half: ", trial_half)

print()
# 2nd half of the string

second_half = str[5:10] # Jamun     10-1==> 9--> Jamun
trial_secHalf = str[5:] # Jamun     10-1==> 9--> Jamun

print("Second_Half: ", second_half)         # Jamun
print("Trails_SecHalf: ", trial_secHalf)    # Jamun  