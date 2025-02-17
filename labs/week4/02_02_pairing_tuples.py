### This code creates a random list for you to use
import random

list_length = random.randint(1, 20)
randlist = list()
for i in range(list_length):
    randlist.append(random.randint(1, 100))


# Write a script that takes randlist (a list of numbers) and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.

# Note: This lab might be challenging! Make sure to discuss ask questions
# and get help!  You will need a python function called `sort`

# example input :[1,2,5,1,2]
# example output :[(1,1), (2,2), (5,0)]

#SOLUTION

sorted_list = sorted(randlist)
new_list=[]
the_tupple = ()
for num in sorted_list:
    if len(the_tupple) < 2:
        the_tupple += (num,)
    
    elif len(the_tupple) == 2:
        new_list.append(the_tupple)
        the_tupple = ()
        the_tupple += (num,)
        
print(f"Input:\n{randlist}")
print(f"\nOutput:\n{new_list}")
        
