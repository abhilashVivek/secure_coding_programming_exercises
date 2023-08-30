# write rock-paper-scissors game

# have the user play against the computer
# you can use the random library to select an option for the computer

# use a while loop so the user can play until they win
import random

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_selection = "rock"
elif computer_choice == 2:
    computer_selection = "paper"
else:
    computer_selection = "scissor"

list_options = ["rock","paper","scissor"]

victory = 0
while victory == 0:
    user_selection = input("Choose (rock / paper / scissor): ")
    while user_selection not in list_options:
        user_selection = input("Invalid option!\nChoose (rock / paper / scissor): ")
    print(f"Computer chose: {computer_selection}")
    if user_selection == computer_selection:
        print("Its a tie!")
        continue
    else:
        
        
        if user_selection == "rock":
            if computer_selection == "paper":
                print("You lost! Better luck next time!")
                continue
            else:
                print("Congratulations! You won!")
                break
        elif user_selection == "paper":
            if computer_selection == "rock":
                print("Congratulations! You won!")
                break
            else:
                print("You lost! Better luck next time!")
                continue
        else:
            if computer_selection == "rock":
                print("You lost! Better luck next time!")
                continue
            else:
                print("Congratulations! You won!")
                break          

# you can map each of rock / paper / scissors to an integer from 1 - 3
