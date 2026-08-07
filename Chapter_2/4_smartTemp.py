# take input in celcius and print its equivalent in fahrenheit and kelvin .
# use explicit type conversion and arithmetic operation .
# Formula
    # Fahrenheit = ( C * 9/5 ) + 32
    # Kelvin = C + 273.15

cel = float(input("Enter the Celsius value: "))

# converting celcius to fahrenheit
fahren = (cel*(9/5)) + 32
print("The Fahrenheit Value is: ",fahren)

# converting celcius to kelvin
kelvin = cel + 273.15
print("The Kelvin Value Is: ",kelvin)