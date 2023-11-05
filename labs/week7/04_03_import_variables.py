"""
Try importing not just your previous function, but also variables (from any previous file of your choice.)

"""
import importlib
__01_02_unpack_star_args = importlib.import_module("01_02_unpack_star_args")

print(__01_02_unpack_star_args.first_element)