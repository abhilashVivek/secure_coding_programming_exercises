#Exercise

#Write a python program in which read an integer number less than 7 from user
def take_input():
        while True:
            number = input("Choose a number between 1 and 7: ")
            if number.isnumeric():
                if int(number)<8:
                    if int(number)>0:
                        number = int(number)
                        return number
            print("Error: Invalid Input.")
  
#If the input number is greater than  or equal to 7, then print error message

#If the input is 0 print "Sunday"
#If the input is 1 print "Monday"
#If the input is 2 print "Tuesday"
#If the input is 3 print "Wednesday"
#If the input is 4 print "Thrusday"
#If the input is 5 print "Friday"
#If the input is 6 print "Saturday"
number = take_input()
days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
if number in range(1,8):
    print(f"Day {number} is a {days[number-1]}.")
#Use if-else statements