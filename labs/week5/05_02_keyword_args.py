## Write a function with keyword arguments
## your function can be a mix of positional and keyword arguments
## it must use a default value for the keyword argument.


def rectangle(length, width=10):
    """
    Input:
        length: int
        width: int, defaults to 10

    
    Returns:
        the area of the rectangle
    """
    return length*width

print(f"Using Positional Argument, the area is {rectangle(3,10)}")
print(f"Using Keyword Argument, the area is {rectangle(width = 10, length = 3)}")
print(f"Using default value for width, the area is {rectangle(3)}")