"""
implement a key-lookup procedure for a dictionary

Try to get the key and update the value by n
If an en exception is raised, handle it by creating the key with a default value
if no exception is raised, update the value
Regardless of what happens, print the dictionary
"""

def dict_keylookup(dict, key):
    try:
        dict[key] = dict[key] + ".v1"
    except KeyError:
        dict[key] = "def_val"
    return dict
    
print(dict_keylookup({1:"val",2:"val"},2))
print(dict_keylookup({1:"val",2:"val"},3))