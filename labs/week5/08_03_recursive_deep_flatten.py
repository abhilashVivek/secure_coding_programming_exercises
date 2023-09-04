## write a deep flatten function that works recursively
## earlier we wrote a deep flatten script that would flatten a nested list
## we solved it with an iterative approach (using a for-break loop)
# now solve it with a recursive function!

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

#SOLUTION

def flatten_lists(input_list):
    
    the_list = []
    
    for item in input_list:
        if isinstance(item,list):
            for sub_item in item:
                the_list.append(sub_item)
        else:
            the_list.append(item)
            
   
    #checking if recursion is required
    if any(isinstance(item,list) for item in the_list) == True:
        temp_the_list = [i for i in the_list]       #cannot modify the_list during recursion
        the_list = []
        the_list.extend(flatten_lists(temp_the_list))
    
    return the_list
        
#custom function to print output in a specific format        
def print_custom(list):
    print(f"{list}\n{flatten_lists(list)}\n")
    
    
print_custom(hard_nested_list)
print_custom(many_nests)