# String Basics ----> String Is Immutable---> we can't change the value's in a string

str1 = 'hello'
str2 = "python"
str3 = '''world'''

print(str1)
print(str2)
print(str3)

print()

# Concatenation of String
print("Hello" + "world")    # Concatenation of String with no between space
print(str1 + str2)          # concatenation of String with no between space 
print(str1 + " " + str2)    # concatenation of String with a space between them

print()

# finding length of the string
print(len(str1))            # str1 = "hello" => length = 5


# Indexing of the string
print(str1[0])              # str1[0] = "hello" => first character = "h")
print(str1[1])              # str1[1] = "hello" => second character = "e")
