# You start this journey with a number `n`.
# You have to display a string representation of all numbers from 1 to n,
# but there are some constraints:
# - If the number is divisible by 3, write `Fizz` instead of the number
# - If the number is divisible by 5, write `Buzz` instead of the number
# - If the number is divisible by both 3 and 5, write `FizzBuzz` instead of the number

# feel free to adjust n for debugging
n = 100

        #i am assuming that you want the numbers and words in a single line without new line characters
the_list = []

for num in range(1,n+1):
    if num % 3 == 0:
        if num % 5 == 0:
            the_list.append( "FizzBuzz")
        else:
            the_list.append( "Fizz")
    elif num % 5 == 0:
        the_list.append( "Buzz")
    else:
        the_list.append( str(num))
the_string = ""
for i in the_list:
    the_string = the_string + i + " "
    
print(f"The required string of numbers is\n'{the_string}'")