# Make your list flatten code do a DEEP flatten and account for other datatypes

hard_nested_list = [
    [1, 2, [1, [1, 2], 2], 3, 4],
    [5, 6],
    [7, 8, 9],
    "shiva",
    10,
    [1, 2, [8, 9,], "Devi"],
    10.0,
    (1, 2),
]

# should get back
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'brandon', 10, 10.0, 1, 2]

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']



#SOLUTION-1
not_a_nested_list = [i for i in hard_nested_list]

loop_condition = True
while loop_condition == True:
    temp_list = []
    for item in not_a_nested_list:
        if isinstance(item,list):
            for sub_item in item:
                temp_list.append(sub_item)
        else:
            temp_list.append(item)
            
    not_a_nested_list = [i for i in temp_list]
    
    #checking if relooping is required
    loop_condition = any(isinstance(item,list) for item in not_a_nested_list)

print(f"{hard_nested_list}\n{not_a_nested_list}")
        