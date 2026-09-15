# Break in python is a statemtn stops the loop immediately when it is encountered.
for num in range(1,10):
    if num == 5:
        print("num is stoped in number 5")
        break
    print(num)

print()

# Continue statement skips the current alteration and moves the next one
for n in range(1, 6):
    if n == 3:
        print("skiped num is 3 and continued from 4")
        continue
    print(n)

print()

# pass statement does nothing — it’s used as a placeholder when you want to keep a block empty.
for i in range(1, 7):
    pass
    print(i)