import random

list=[1,2,3,4]
print(random.random()) # values between 0 to 1
print(random.randint(3,9)) # prints values in range
print(random.randrange(1,10,2)) # print values in range
print(random.choice(list)) # random values from sequence
print(random.shuffle(list))
print(list)