# Write a script that creates a dictionary of keys, `n`
# and values `n * n` for numbers 1 to 10. For example:
# result = {1: 1, 2: 4, 3: 9, ... and so on}

# use a for-loop

#SOLUTION

output_dict = {}
for i in range(10):
    num = i + 1     #due to zero indexing
    current_dict = {num : num*num}
    output_dict.update(current_dict)
    
print(output_dict)
    