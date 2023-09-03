# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

# NOTE - you make only keep purely unique values from the original list
# i.e. if it appeared more than once in the first list, you have to remove it entirely.

#SOLUTION

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_list = [value for value in list_ if list_.count(value) == 1]

print(unique_list)