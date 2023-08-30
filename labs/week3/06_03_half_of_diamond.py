#Exercise

#Write a Python program to construct the following pattern, using a nested for loop.
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""
for x in range(6):
    for y in range(x):
        print("*",end=" ")
    print()             #prints the first 5 lines

for x in range(4,0,-1):
    for y in range(x):
        print("*",end=" ")
    print()             #prints the last 4 lines
