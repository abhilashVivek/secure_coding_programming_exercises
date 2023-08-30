# Build a CLI RPG game following the instructions from the course.

# Ask the player for their name.
name = input("Enter your name: ")


# Display a message that greets them and introduces them to the game world.
print(f"Hello {name}! Welcome to this CLI RPG game")


# Present them with a choice between two doors.
door_options = ["left","right"]
left_room_options, right_room_options = ["back","look"], ["back","fight"]
sword_found = 0
door = input("Choose a door (left / right) :")




while 2 == 2:       #creating infinite loop to rerun the code from lobby
    user_response = "Value yet to be reassigned."
    while door not in door_options:
        door = input("Invalid input.\nChoose a door (left / right) :")
        
        
# If they choose the left door, they'll see an empty room.
    else: 
        if door == "left":          #left door code
            print("The room seems empty!")
            while user_response not in left_room_options:
                user_response = input("Do you want to go back or look around?\nEnter (back / look): ")
            if user_response == "look":
                print("You found a sword!\nYou are being sent back to the lobby")
                sword_found = 1
                door = input("Choose a door (left / right) :")
                continue
            else:
                print("You are in the lobby!")
                door = input("Choose a door (left / right) :")
                continue
            continue
        
        
# If they choose the right door, then they encounter a dragon.


        else:           #right door code
            print("There is a dragon in the room!")
            if sword_found == 0:          #entering dragons room without a sword
                while user_response not in right_room_options:
                    user_response = input("Do you want to go back or fight?\nEnter (back / fight): ")
                if user_response == "fight":
                    print("You have been killed by the dragon!\nGame Over!")
                    break
                else:
                    print("You are in the lobby!")
                    door = input("Choose a door (left / right) :")
                    continue
                continue
            
            
            else:           #entering dragons room with a sword
                while user_response not in right_room_options:
                    user_response = input("Do you want to go back or fight?\nEnter (back / fight): ")
                if user_response == "fight":
                    print("You have slayed the dragon!\nMission Completed!")
                    break
                else:
                    print("You are in the lobby!")
                    continue
                continue
            continue
        continue
                
# In both cases, they have the option to return to the previous room or interact further.

# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.

# When encountering the dragon, they have the choice to fight it.

# If they have the sword from the other room, then they will be able to defeat it and win the game.

# If they don't have the sword, then they will be eaten by the dragon and lose the game.
