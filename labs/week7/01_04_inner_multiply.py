# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]

def the_func(*args):
    list1 = []
    for i in args:
        a,b = i
        list1.append(a*b)
    return list1

print(the_func((1,2), (2,2), (3,2), (4,5)))
