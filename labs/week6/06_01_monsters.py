"""
Write 3 classes which are related to each other
1) a monster class
2) a night-monster class (they only come out at night)
3) a full moon monster class (they only come out at night and on the full moon)

Make use of inheritance to save your code!

## Monster class
# class attribute
time_of_day (will need to activate night monsters)
day_of_month
full_moon (boolean)

# attributes
name
number of limbs
attack mode (magic, physical, mental hypnosis etc)
scare factor
weakness
life points

# methods
basic attack (attack something)
sleep (get life points back)
defend (something attacks it!)

## Night monster
same as above, but also special powers that activate at night
vulnerable in daylight


## full moon monster
only active in the full moon
"""

class Monster:
    # Class attribute
    time_of_day = "day"
    day_of_month = 1
    full_moon = False

    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points):
        # Attributes
        self.name = name
        self.limbs = limbs
        self.attack_mode = attack_mode
        self.scare_factor = scare_factor
        self.weakness = weakness
        self.life_points = life_points

    def basic_attack(self, target):
        # Basic attack method
        print(f"{self.name} uses {self.attack_mode} to attack {target}.")
        # Implement attack logic here

    def sleep(self):
        # Sleep to regain life points
        self.life_points += 10
        print(f"{self.name} sleeps and regains 10 life points.")

    def defend(self, attacker):
        # Defend against an attack
        print(f"{self.name} defends against {attacker}.")
        # Implement defense logic here


class NightMonster(Monster):
    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points, special_powers):
        super().__init__(name, limbs, attack_mode, scare_factor, weakness, life_points)
        self.time_of_day = "night"
        self.special_powers = special_powers
        self.vulnerable_in_daylight = True

    def use_special_powers(self, target):
        # Use special powers during the night
        if self.time_of_day == "night":
            print(f"{self.name} uses special powers to affect {target}.")
            # Implement special power logic here
        else:
            print(f"{self.name} is vulnerable in daylight and cannot use special powers.")


class FullMoonMonster(NightMonster):
    def __init__(self, name, limbs, attack_mode, scare_factor, weakness, life_points, special_powers):
        super().__init__(name, limbs, attack_mode, scare_factor, weakness, life_points, special_powers)
        self.full_moon = True

    def use_special_powers(self, target):
        # Use special powers during a full moon night
        if self.full_moon:
            print(f"{self.name} uses special powers during the full moon to affect {target}.")
            # Implement full moon special power logic here
        else:
            print(f"{self.name} is only active during the full moon and cannot use special powers now.")
