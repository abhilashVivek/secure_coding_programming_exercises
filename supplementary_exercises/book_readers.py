# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with the last two words of the text of `war_and_peace.txt`
# 3) Loop over all three files and print out only the first word of each.

#TASK-1
with open(r"supplementary_exercises\books\war_and_peace.txt", "r",encoding="utf-8") as the_file:
    file_string = the_file.read()
    
#TASK-2
temp_list = list(file_string.split(" "))        #converting into list to detect words.

with open(r"supplementary_exercises\books\crime_and_punishment.txt", "w") as the_file:
    the_file.write(temp_list[-2] + " " + temp_list[-1])
    
#TASK-3
file_list = [r"supplementary_exercises\books\war_and_peace.txt" ,
             r"supplementary_exercises\books\crime_and_punishment.txt" ,
             r"supplementary_exercises\books\pride_and_prejudice.txt"]       #creating a list for iteration

for path in file_list:
    with open(path, "r",encoding="utf-8") as the_file:
        file_string = the_file.read()
        temp_list = list(file_string.split(" "))
        print(f"The first word from '{path}' is:   '{temp_list[0]}'")