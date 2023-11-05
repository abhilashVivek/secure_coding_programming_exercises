"""
Write a function that accepps the following arguments
INPUT:
    name: str
    job : str
    * args: adjectives (str) that describe things (i.e "happy", " sad")
    **args: possessions (str): value (int / float)
Output:
   Form a  nice string that explains everything relevant



example input:
   ('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20)
output:
   "Gilad is a teacher who is happy, amazing, and sooooo cool. Gilad has a bike worth 2000, a house worth 1000, and shoes with 20"


The string should accomadate any number of *args and **kwargs.
"""
def the_func(name,job,*args,**kwargs):
   the_string = f"{name} is a {job} who is {args[0]}"
   for i in args[1:-1]:
      the_string = the_string + ", " + i
   the_string += f" and {args[-1]}. {name} has"
   list_of_kwarg_strings = []
   for k,v in kwargs.items():
      list_of_kwarg_strings.append(f"a {k} worth {v}")
      
   the_string += f" {list_of_kwarg_strings[0]}"
   for i in list_of_kwarg_strings[1:-1]:
      the_string = the_string + ", " + i
   the_string += f" and {list_of_kwarg_strings[-1]}."
   
   return the_string

print(the_func('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20))
   