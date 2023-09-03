# Use a list comprehension to create a list that contains the individual
# letters of the word "codingnomads":
# ['c', 'o', 'd', 'i', 'n', 'g', 'n', 'o', 'm', 'a', 'd', 's']
#
# Note: You can solve this more quickly with a call to `list()`
# but try to do it using a list comprehension.

word = "Amrita Vishwavidyapeetham"

#SOLUTION

# i am gonna assume that you want us to ignore blank spaces

list1 = [letter for letter in word if not letter == " "]

print(list1)