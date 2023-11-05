""""
import the math library and use it to automatically generate a random list of numbers
You should generate 1000 random numbers.


"""
import random

random_nums = []
for i in range(1000):
    random_nums.append(random.randint(0,9))
    
print(random_nums)