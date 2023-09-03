# Exercise

# Write a program to move all zero digits to end of a given list of numbers
# Expected output:
# Original list:

# [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:

# [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#SOLUTION

the_list = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
print(the_list)
number_to_move = 0
count_of_the_number_to_move = the_list.count(0)
new_list =[]

for i in the_list:
    if i != 0:
        new_list.append(i)

for i in range(count_of_the_number_to_move):
    new_list.append(0)

print(f"After moving all {number_to_move}s to the end. The updated list is...\n{new_list}")