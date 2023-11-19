"""
Write a function that takes two inputs and attempts to add them together.

Use a try/except block to catch all possible errors

Try adding
int + int
int + str
str + list
tuple + list
dict + dict
dict + str

Are all the exceptions the same?
"""
def take_add():
    x, y = input("Enter first element: "), input("Enter second element: ")
    try:
        if (type(x) == type(1) and type(y) == type(1)):
            x = int(x)
            y = int(y)
        elif (type(x) == type(1.0) and type(y) == type(1.0)):
            x = float(x)
            y = float(y)
        return x + y
    except TypeError:
        print(f"The '+' operation is not possible between {type(x)} and {type(y)}")
        
take_add()