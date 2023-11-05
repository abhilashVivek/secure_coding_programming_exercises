"""
Update your chicken class to include the following dunders

__str__  : make some nice str format for your chicken. 
When we print your chicken it should tell us: how heavy the chicken is, the gender and how many eggs it has laid (if has)

__add__ : what happens when you add two chickens together? If they are male and female, create a baby chicken! (a new chicken) Otherwise, nothing?

"""

import random

class chicken:
    
    def __init__(self):
        self.number_of_chickens = int(input("Enter the total number of chickens: "))
        self.chicken_attributes()
        
                   
    def chicken_attributes(self):      #function to determine average
        
        self.egg_count = 0
        self.male_count = 0
        self.female_without_eggs_count = 0
        self.female_with_eggs_count = 0
        
        
        for i in range( self.number_of_chickens):
            self.weight = random.randint(5,11)       #pounds
            self.breed = random.choice(["Rhode Island Red", "Leghorn", "Plymouth Rock", "Australorp", "Wyandotte"])
            
            
            self.gender = random.choice(["male","female"])
            self.night = random.choice([True,False])
        
            #using random generator to determine number of eggs laid
            self.lays_eggs = (random.choice([True,False]) if self.gender == "female" else False)
            self.number_of_eggs_laid = (random.randint(1,3) if self.lays_eggs == True and self.night == True else 0)
        
            
            if self.gender == "female":
                if self.lays_eggs:
                    self.egg_count += self.number_of_eggs_laid
                    self.female_with_eggs_count += 1
                else:
                    self.female_without_eggs_count += 1
            else:
                self.male_count += 1
            
            
            #prints chicken detail string    
            print(f"'{self.breed}' chicken, weighing '{self.weight}' pounds, laid '{self.number_of_eggs_laid}' eggs.")
                
        average_eggs_laid = self.egg_count // self.female_with_eggs_count
        
        # print(f"Out of '{ self.number_of_chickens}' chickens,\n'{self.male_count}' were male and '{self.female_without_eggs_count}' couldnt lay eggs.")
        # print(f"The daily average eggs laid by the remaining '{self.female_with_eggs_count}' chickens = '{average_eggs_laid}'")

x= chicken()