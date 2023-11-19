"""
Write a function that accepts user input with the input() function
Specify that they must use alphabet characters only.
Then raise an exception if they enter anything that is not able an alphabet character!

Hint: you can use .isalpha() to check if a character is an alpha character.
"""
def acc_inp():
    the_input = input("Please enter alphabeic input: ")
    if not the_input.isalpha():
        raise Exception ("Your input is not alphabetic.")
        
acc_inp()
        
    