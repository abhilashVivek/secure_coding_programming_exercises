#Open the csv_practice_users.csv doc
#Retrieve all names that start with an S
#Add the ages of all the users print the total
#Retrieve the phone number of the user Jay 
import csv

with open(r"supplementary_exercises\csv_practice_users.csv", 'r') as csv_file:      #opening file
    csvreader = csv.reader(csv_file)
    print("- The names starting with S are:",end=" ")
    for row in csvreader:
        if row[0].startswith("S") or row[0].startswith("s"):        #printng names starting with an S
            print(row[0],end=" ")

with open(r"supplementary_exercises\csv_practice_users.csv", 'r') as csv_file:      #opening file
    csvreader = csv.reader(csv_file)    
    total_age = 0           #declaring age variable type
    for row in csvreader:
        if row[1].isnumeric():
            total_age += int(row[1])
    print(f"\n- The total age is:  '{total_age}'")             #printing sum of all the ages
    
with open(r"supplementary_exercises\csv_practice_users.csv", 'r') as csv_file:      #opening file
    csvreader = csv.reader(csv_file)    
    for row in csvreader:
        if row[0].startswith("Jay"):
            print(f"- Jay's phone number is:  '{row[2]}'")