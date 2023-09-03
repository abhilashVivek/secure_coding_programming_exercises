# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [1, 2, 6, 55, 'hi', 4, 13,]

#SOLUTION
#copying list_ from top
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = []
for item1 in list_:
    item_count = 0
    for item2 in list_:
        if str(item1) == str(item2):         #converting to string to avoid type error
            item_count +=1
    if item_count == 1:
        unique_list.append(item1)

print(list_)
print(f"The unique items in the above list are..\n{unique_list}")