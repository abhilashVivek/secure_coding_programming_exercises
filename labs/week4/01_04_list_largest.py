# Exercise

# Write a program to find the largest number in a list without using built-in functions

# [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
# output = 123123

# use a for loop


#SOLUTION

the_list = [1,2,1,3,123123,2,1,3,6,3,1,23,6,123,1235,]
largest_num = 0
for item1 in the_list:
    for item2 in the_list:
        if item1 > item2:
            if largest_num < item1:
                largest_num = item1
                
print(the_list)
print(f"The largest number is '{largest_num}'.")

#This code works under the assumption that the_list contains float or integer type items
