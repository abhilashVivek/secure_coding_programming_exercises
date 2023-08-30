# Exercise

# Write a program to print the even numbers from 0 to 100 using for loop and without using if-else
start, end = 0, 100
list = []
for even_num in range(start,end+1,2):
    list.append(even_num)
print(f"Even numbers between {start} and {end} are\n{list}")