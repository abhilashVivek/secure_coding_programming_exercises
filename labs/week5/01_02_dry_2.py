# rewrite your function from the previous exercise (01_01_dry.py)
# this time your function should be able change the divisible by number.

# I should be able to return the list of numbers which is divisible by "n", where
# 'n' can be any number.

## Input: a list of integers, a number 'n'
## output: a new list that only has retains numbers which are divisible by n


#SOLUTION:

#INPUT
other_numbers = [213, 2, 3, 125, 12, 32, 21, 3, 6, 23, 12, 3, 326, 45, 12, 32, 14, 2]
divisible_by = 3

#FUNCTION
def extract_num(numbers,divisible_by):
    div_2 = []
    for i in numbers:
        if i % divisible_by == 0:
            div_2.append(i)
    print(div_2)
    return div_2

extract_num(other_numbers,divisible_by)