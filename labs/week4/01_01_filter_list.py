# Exercise

# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3


## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


#SOLUTION -STAGE1

# copying the sample list privided on top
sample_list = ['aaaa', 'a', 'ab', 'abc']
#iterating through the list
result_count = 0
for item in sample_list:
    if len(str(item)) >= 2:
        result_count += 1
print(sample_list)
print(f"'{result_count}' items in the list match STAGE-1 parameters.")
print()

#SOLUTION -STAGE2

#reassigning variables for reuse
# copying the sample list privided on top
sample_list = ['abc', 'xyz', 'aba', '1221']
result_count = 0

for item in sample_list:
    if len(str(item)) >= 2:    
        if item[0] == item[-1]:
            result_count += 1
print(sample_list)
print(f"'{result_count}' items in the list match STAGE-2 parameters.")