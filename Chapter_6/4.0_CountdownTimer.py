# Countdown Timer (with 1-second gap)
# Print a countdown before something “exciting” happens (like “Launching...” or “Happy New Year!”).
# Concepts Used: for loop, range(), and the time module.

import time

countnum = int(input("Enter a coutdown number: "))

print("Countdown Starts Now: \n")

for i in range(countnum, 0, -1):
    print(i)
    time.sleep(1)
print("Happy New Year")
