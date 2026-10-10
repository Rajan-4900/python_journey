# 1Q. write a function Square(num) that returns the square of a number.
def square(num):
    return  num ** 2

print(square(5))    # Output: 25

print("\n")

# 2Q. write a function that takes a string and returns the count of vowels and consonant separately.
def count_vowels(userInput):
    #define vowels
    vowels = "aeiou AEIOU"

    # consonents
    countVowels = 0
    countConsonent= 0

    # Example Word : Rajan
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowels += 1
            else :
                countConsonent += 1

    return countVowels, countConsonent
# Function Call 
vowels, consonants = count_vowels("Rajan")
print(f"Vowels: {vowels}, Consonants: {consonants}")        # Output: Vowels:  2
    
# 3Q. define a function converts_to_upper(word) that returns the uppercase version of the string 
def convert_to_upper(word):
    return word.upper()

print(convert_to_upper("rajan"))    # Output: RAJAN

# 4Q. create a function full_nane (fname, lname) that returns the full name joined with a space
def full_name(fname, lname):
    return fname + " " + lname

FullName = full_name("Rajan", "L")
print(FullName)    # Output: Rajan L