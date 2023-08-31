# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it


#SOLUTION

#this section can be changed . a list of dictionary can be added to randomize the words
word = "candle"
print("I'm tall when I'm young, and I'm short when I'm old. What am I?")
retry_counter = 5

#welcome message
player_name = input("Please enter your name: ")
print(f"Welcome {player_name}!\nYou have '{retry_counter}' attempts to guess the correct word.")
predictions = []



#defining a function to print the revelation of the word
def print_status(x=word,y=predictions):
    for character in x:
        if character not in y:
            print("_", end=" ")
        else:
            print(character,end=" ")
    print()

#looping through input according to required parameters
while len(predictions) != len(word):
    print_status(word,predictions)
    predicted_char = input("Guess a character: ")
    if len(predicted_char) != 1:
        print("Multiple characters not allowed! Try again.")
        continue
    
    if not predicted_char.isalpha():
        print("Only english alphabets allowed! Try again.")
        continue
    
    if not predicted_char in word:
        if retry_counter > 0:
            print(f"Incorrect guess! Try again\nPS.: You have {retry_counter} attempts remaining.")
            retry_counter -= 1
            continue
        else:
            print("Mission failed! Better luck next time")
            print(f"The word was '{word}'.")
            break
        continue
    
        
    if predicted_char in word and not predicted_char in predictions:
        print("Correct guess!")
        predictions.append(predicted_char)
        continue
    else:
        print("You have already guessed this alphabet.")
        continue

if len(predictions) == len(word):
    print("You are right! The word is...")
    print_status(word,predictions)
