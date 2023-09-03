# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

# SOLUTION
output_dict = {}

for key in dict_1:
    if key in dict_2:
        output_dict.update({key : dict_1.get(key) + dict_2.get(key)})
    else:
        output_dict.update({key : dict_1.get(key)})

for key in dict_2:
    if not key in dict_1:
        output_dict.update({key : dict_2.get(key)})

print(output_dict)       