# use a while loop to sum all the numbers from 1 - 100
start, end = 1, 100         #values can be changed


sum=0
num = start
while num in range(start,end+1):
    sum += num
    num += 1
print(f"The sum of all the numbers from {start} to {end} is '{sum}'.")