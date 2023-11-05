"""
create a simple bicylce class

# Attributes
number of tires
type of of tires (road vs mountain bike)
model
color
number of speeds
brakes (front or back or both)
current speed.

# Methods
brake
pedal faster (should affect speed)
"""

class bicycle:
    def __init__(self,intial_speed,operation,seconds):
        self.initial_speed = intial_speed
        self.braking_rate = 2
        self.acceleration_rate = 2
        self.operation = operation
        self.seconds = seconds
        self.brake = ["brake","urgent_brake"]
        self.pedal = ["keep_pedalling","pedal_faster","full_throttle"]
    def braking(self):
        if self.operation == self.brake[0]:
            final_speed = self.initial_speed - (self.braking_rate)*self.seconds
        elif self.operation == self.brake[-1]:
            final_speed = self.initial_speed - (self.braking_rate * 10)*self.seconds
        if final_speed > 0:
            return final_speed
        else:
            final_speed = 0
            return final_speed
    def acceleration(self):
        if self.operation == self.pedal[-1]:
            final_speed = self.initial_speed + (self.acceleration_rate*2)*self.seconds
        elif self.operation == self.pedal[-3]:
            final_speed = self.initial_speed
        elif self.operation == self.pedal[-2]:
            final_speed = self.initial_speed  + self.acceleration_rate*self.seconds
        return final_speed
    
my_bicycle = bicycle(int(input("Initial speed: ")),input("Select operation:\n(brake / urgent_brake / keep_pedalling / pedal_faster / full_throttle): "),int(input("Enter operation time in seconds:")))
print(f"The bicycles speed is now {my_bicycle.acceleration()} kmph.")