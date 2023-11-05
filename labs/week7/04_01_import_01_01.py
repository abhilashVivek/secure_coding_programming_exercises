"""
Import your function from 01_01_sum_ints_inf_args.py
and use it here

Go back into your code and stop your print statements from showing up here

"""
import importlib
_01_01_sum_ints_inf_args = importlib.import_module("01_01_sum_ints_inf_args")

#had to do it because file name starts with a number
print(_01_01_sum_ints_inf_args.sum_ints(1,2,3,4,'hi','hi',(1,2,3), 10))