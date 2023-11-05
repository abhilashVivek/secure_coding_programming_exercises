# write a function that takes two positional arguments and uses *args
# your function should:
"""
arguments:
    name: name of person
    job: job title of person
    *args: possesions that they own

returns --> Str
   It should return a string that says a nice message like
  "hello Gilad, I heard your job of washing dishes allows you to own a lawn-mower, house, cat, and bat"

Remember, your string needs to _grow_ with the *args - it needs infinite potential!

"""

def concat_custom(name,job,*args):
  the_string = f"hello {name}, I heard your job of {job} allows you to own a {args[0]}"
  for i in args[1:-1]:
    the_string = the_string + ", " + i
  return the_string + " and " + args[-1] +"."

print(concat_custom("Gilad","washing dishes","lawn-mower", "house", "cat","bat","anything else you want"))