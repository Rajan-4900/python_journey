# Nested Dictionary 

profile = {
    "Name": "Rajan",
    "Age": 21,
    "ClgDetails" : {
        "ClgAddr": "PipeLine",
        "USN" : 402,
        "Branh" : "CSE" 
    }
}

print(profile)
print(profile["ClgDetails"])
print(profile["ClgDetails"]["USN"])