# Exercise

# Write an explicit infinite loop
# inside the infinite loop, read integer from user as an option

# If the option is 1: print here is your first step
# If the option is 2: print "you have some steps to go"
# If the option is 3: print "you are almost done"
# If the option is 4: quit from the loop

# If the option is other number: print it is an  invalid option
while True:
    num = input("Enter number: ")
    if num.isnumeric():
        num = int(num)
        if num in range(1,4):
            if num == 1:
                print("here is your first step")
                continue
            if num == 2:
                print("you have some steps to go")
                continue
            if num == 3:
                print("you are almost done")
                continue
        elif num == 4:
            print("Exiting loop")
            break
    else:
        num = input("Invalid input. Try again.\nEnter number: ")
