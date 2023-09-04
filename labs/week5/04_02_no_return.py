# write a function that does not return any variable!


def print_your_name_UPPER(name):
    """
    input: str (a name)
    output: None # no return!

    This function Prints out the users name in all uppercase
    """
    local_varible = name.upper      #output will be null becuse the return command is not used.
                                    # so the function only stores the converted value locally
    # print(local_varible)            #however if i use the print command, the code will show an output


# What happens when you run your function and attempt to return a variable?
a = print_your_name_UPPER("lower case name")
# what is a?
