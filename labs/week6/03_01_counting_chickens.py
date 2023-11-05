"""
create a chicken class that has the following

# class attributes
time_of_day
number_of_eggs_laid

# instance attributes (uses the self variable)
breed
gender
weight
lays_eggs (boolean)

# methods
lay_egg --> this function should depend on time of day (chickens only lay eggs at night!),
it should also use random numbers to deterimine if laying the egg worked or not


## Create 100 instances of your chickens using a for loop

Use a for loop to update the time of day (go through each hour of the day)
within the loop have your chickens all try to lay eggs
Afterwards, print out how many total eggs were hatched -- for all chickens and individually.
What was the average number of eggs per chicken?
"""
import random

class chicken:
    
    def __init__(self):
        self.number_of_chickens = int(input("Enter the total number of chickens: "))
        self.average_eggs()
        
                   
    def average_eggs(self):      #function to determine average
        
        self.egg_count = 0
        self.male_count = 0
        self.female_without_eggs_count = 0
        self.female_with_eggs_count = 0
        
        
        for i in range( self.number_of_chickens):
            self.weight = random.randint(5,11)       #pounds
            self.breed = random.choice(["Rhode Island Red", "Leghorn", "Plymouth Rock (Barred Rock)", "Australorp", "Wyandotte", "Orpington", "Sussex", "Brahma", "Silkie", "Easter Egger", "Ameraucana", "Cochin", "Hamburg", "Marans", "Jersey Giant"])
            
            
            self.gender = random.choice(["male","female"])
            self.night = random.choice([True,False])
        
            #using random generator to determine number of eggs laid
            self.lays_eggs = (random.choice([True,False]) if self.gender == "female" else False)
            self.number_of_eggs_laid = (random.randint(1,4) if self.lays_eggs == True and self.night == True else 0)
        
            
            if self.gender == "female":
                if self.lays_eggs:
                    self.egg_count += self.number_of_eggs_laid
                    self.female_with_eggs_count += 1
                else:
                    self.female_without_eggs_count += 1
            else:
                self.male_count += 1
                
                
        average_eggs_laid = self.egg_count // self.female_with_eggs_count
        
        print(f"Out of '{ self.number_of_chickens}' chickens,\n'{self.male_count}' were male and '{self.female_without_eggs_count}' couldnt lay eggs.")
        print(f"The daily average eggs laid by the remaining '{self.female_with_eggs_count}' chickens = '{average_eggs_laid}'")

x= chicken()