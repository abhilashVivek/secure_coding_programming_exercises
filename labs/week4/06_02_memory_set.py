# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

# you will need the `input()` function to collect information from the user


#SOLUTION

#PARAMETERS
num_set = set()
set_len = 10
error_count = 5


while not len(num_set) == set_len:
    num_input = input("Enter a number:")
    while not num_input.isnumeric():
        num_input = input("Invalid input! Enter a valid number:")
    

    if int(float(num_input)) in num_set:
        error_count -= 1
        print(f"Duplicate entry!\nYou have '{error_count}' attempts remaining.")
        if error_count <= 0:
            print("Mission failed!")
            break
        
    else:
        num_set.add(int(float(num_input)))
        print(f"{num_input} added successfully!\nAdd '{set_len - len(num_set)}' more numbers.")
    continue

else:    
    print(f"Congratulations! '{len(num_set)}' numbers have been added!")
    print(f"Your set is..\n{num_set}")