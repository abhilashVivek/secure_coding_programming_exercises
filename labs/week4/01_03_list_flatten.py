#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

#SOLUTION

sample_input = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_list = []
for item in sample_input:
    if type(item) == type(sample_input):
        for sub_items in item:
            new_list.append(sub_items)
    else:
        new_list.append(item)
        
#This code flattens the list upto one level. to increase the levels we have to nest more conditions
print(sample_input)
print(f"After flattening the updated list is..\n{new_list}")