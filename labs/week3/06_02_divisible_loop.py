# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700
start, end = 1500, 2700
list = []
for num in range(start,end+1):
    if num % 7 == 0:
        if num % 5 == 0:
            list.append(num)
print(f"The numbers divisible by 7 and multiples of 5 are:\n'{list}'")