# A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a 
# block of code for each item in that sequence. It is often used when the number of iterations is known beforehand.

bikes = ["Duke", "KTM", "Royal Enfield", "Yamaha", "ZX-10R"]

# print(bikes[0])
for model in bikes:
    print(model)  # This will print each bike model in the list

# Range Value : 
# for i in range(start, stop, step):
# start---> starting of the index/number/Value/String
# stop ---> end of the index/number/value/String
# step ---> it will increase the step (like ex: step = 2, it will print 2 steps 2,4,6,8,10....)

for item in range(2, 20, 1):
    print(item)  # This will print numbers from 2 to 19 (20 is not included)

