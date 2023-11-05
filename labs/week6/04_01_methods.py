"""
Create a class (you pick the name) that has
at least 5 methods.
3 of the methods must call other methods within them (using self.method name)
Run at least one method automatically in __init__ so it will run at start up

Demonstrate your methods work by creating an instance and running all the methods
"""
class the_class:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        self.addition()    
    
    def addition(self):
        print(self.num1," + ",self.num2," = ",self.num1+self.num2)
        self.subtraction()
    
    def subtraction(self):
        print(self.num1," - ",self.num2," = ",self.num1-self.num2)
        self.multiplication()
        
    def multiplication(self):
        print(self.num1," x ",self.num2," = ",self.num1*self.num2)
        self.division()
        
    def division(self):
        print(self.num1," / ",self.num2," = ",self.num1//self.num2)
        
x = the_class(10,5)
