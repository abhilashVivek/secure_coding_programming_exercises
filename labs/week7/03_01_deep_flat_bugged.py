# debug this code
# I broke all kinds of things. NOTHING is safe !!!


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
# [1, 2, 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 'shiva', 10, 1,2,8,9, "Devi", 10.0, 1, 2]

many_nests = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", "h"]
# should get back
# ['a', 'bb', 'ccc', 'ddd', 'ee', 'ff', 'g', 'h']

def deep_flatten(list1):
    while True:
        final_list = []
        for element in list1:
            if isinstance(element, (list, tuple)):
                final_list.extend(element)
            else:
                final_list.append(element)

        for elem in final_list:
            if isinstance(elem, (tuple, list)):
                list1 = final_list
                break 
        else:
            return final_list
        
print(f"{many_nests}\n{deep_flatten(many_nests)}")
print(f"{hard_nested_list}\n{deep_flatten(hard_nested_list)}")

