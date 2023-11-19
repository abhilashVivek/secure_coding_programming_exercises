"""
rewrite inner_multiple from  Week 8

# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]


Iterate over the args summing them up. 
Use an if statement ot check if the user passed tuples.
Raise an exception if they passed something else
"""

def the_func(*args):
    for arg in args:
        if not type(arg) == type((1,1)):
            raise Exception ("All args are not tuples!")
    list1 = []
    for i in args:
        a,b = i
        list1.append(a*b)
    return list1


print(the_func((1,2), (2,2), (3,2), (4,5),["new item to test exception"]))
