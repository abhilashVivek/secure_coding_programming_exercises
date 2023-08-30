# write a short command line game

# 1. ask the user for their name: (use the input() function)
name = input("Enter your name: ")
name = name.title()
# Say hello to them with their name
print(f"Hello, {name}.")
vowels = ("A","E","I","O","U") 
# If their name begins with a vowel say something funny about that ("Aha! Oho! Uhu! Ihi! etc", your name begins with a vowel!)
if name.isalpha() == True:
    if name.startswith(vowels):
        print("Aha! I see that your name starts with a vowel.\nYou know, I once had an argument with a friend about which vowel is the most important.\nI won!")
# If their n ame begins with a consonant make an even better joke about it.
    else:
        print("I see your name starts with a consonant.\nSo tell me, how does it feel to be disemvoweled?")
else:
    print("I see your name starts with a number.\nDo you know why 6 is afraid of 7?\nBecause... 7 8 9.")    
# Ask them to pick a number between 1 and 10.
# If they guessed the right number, tell them they won
# Else, tell them they lost.
number = input("Jokes apart. Pick a number between 1 and 10: ")
while number.isnumeric() != True:
    number = input("Pick a number between 1 and 10: ")
else:
    number = int(float(number))
import random

random_number = random.randint(0, 11)
if number == random_number:
    print("Congratulations! You won!")
else:
    print("You lost. Better luck next time!")
