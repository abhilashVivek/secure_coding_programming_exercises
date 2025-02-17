## write a function that uses **kwargs as input
## it should print out the sum of all the integers found in the values

"""
input: hi = 2020, bye = 1000, see = 2, def = 'this'
output : 3022

The function should work for any kind of values and as many keyword arguments as the use would like to pass

"""
def the_func(**kwargs):
    sum1 = 0
    for k,v in kwargs.items():
        if type(v) == type(1):
            sum1 += v
    return sum1

print(the_func(hi = 2020, bye = 1000, see = 2, def1 = 'this'))
            
