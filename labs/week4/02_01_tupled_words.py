# create a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

#SOLUTION

input = "hello world"
l1 = input.split()
l2 = []

for word in l1:
    t1 =()
    for character in word:
        t1 += (character,)
    l2.append(t1)
    
print(f"input = {l1}")
print(f"result_list = {l2}")