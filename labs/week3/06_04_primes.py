# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it
start, end = 0, 100             #code will work even after changing start end values
list=[]                         #list to add all prime numbers
for num in range(start,end+1):          #iterates from 1 to 100
    divisor_count = 0
    for divisor in range(1,num+1):
        if num % divisor == 0:
            divisor_count += 1
    if divisor_count == 2:
        list.append(num)
print(f"The prime numbers between 1 and 100 are:\n{list}")