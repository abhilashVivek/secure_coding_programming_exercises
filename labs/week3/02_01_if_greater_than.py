# Exercise

# Write a program by accepting 2 numbers from the user and check number is greater than other and print the result
# you can use the functionfg `input()` to get user input
num1,num2 ="not numeric","also not numeric"
while num1.isnumeric() != True and num2.isnumeric() != True:
    num1= input("Enter num1: ")      
    num2= input("Enter num2: ")
    
# example
# first_number = input("please enter a number: ")
# second_number = input("please enter another number!: ")
if num1 > num2:
    print("The first number:",num1,"is greater than the second number:",num2)
elif num2 > num1:
    print("The second number:",num2,"is greater than the first number:",num1)
else:
    print ("Both the numbers are equal.")
# print(first_number)

# note, what type is your first_number? Is it what you expected?
# look-up the input() docume ntation to find out what type it will create by default
