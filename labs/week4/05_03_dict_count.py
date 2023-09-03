# Exercise

# Write a program to create a dictionary from a string.
# Track the count of the letters from the string.
# Sample string : 'securecoding'
# Expected output: {'s': 1, 'e': 2, 'c': 2, 'u': 1, 'r': 1, 'o': 1, 'd': 1, 'i': 1, 'n': 1, 'g': 1}


#SOLUTION

input_string = 'securecoding'

#removing duplicates from string
list_input_string = []
for i in input_string:
    list_input_string += i
updated_string = ""
for i in list_input_string:
    updated_string += i
    
#creating dictionary
output_dict = {}
for character in updated_string:
    current_dict = {character : input_string.count(character)}
    output_dict.update(current_dict)
    
print(output_dict)