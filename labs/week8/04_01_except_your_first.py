"""
Write a function that accepts user input with the input() function
Try to convert their input to `int` and catch any exceptions that happen.

what kind of exceptions did you find?

"""
def take_input():
    x = input("Please enter an integer: ")
    try:
        x = int(x)
    except ValueError:
        print(f"'{x}, is not a valid integer.")

        
take_input()