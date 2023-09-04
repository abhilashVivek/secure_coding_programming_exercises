# Write a function that returns multiple values
# example idea:


def lower_names(first_name, last_name):
    """
    Input:
        first_name: str
        last_name: str
    returns:
        first_name, last_name 

    This function takes the first name and last name and lowercases them

    example input: GILAD GRESSEL
    output: gilad gressel
    """
    return first_name.lower(),last_name.lower()


# what happens when you return multiple variables ?

first, last = lower_names("GILAD", "GRESSEL")  # how does this work?
print(first, last)
names = lower_names("GILAD", "GRESSEL")  # what datatype is names?
print(names)         #names is a tuple

