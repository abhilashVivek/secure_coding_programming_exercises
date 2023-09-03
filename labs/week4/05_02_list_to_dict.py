# Exercise

# Write a Python program to convert the nested list to a list of dictionaries

# Sample lists: [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]

# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
#                   {'color_name': 'Red', 'color_code': '#FF0000'},
#                   {'color_name': 'Maroon', 'color_code': '#800000'},
#                   {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# use a for-loop

#SOLUTION
the_list = [["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]]

new_list = []
for a in the_list[0]:
    b= the_list[0].index(a)
    dict1 ={"color_name" : a , "color_code" : the_list[1][b]}
    new_list.append(dict1)
    
print(new_list)