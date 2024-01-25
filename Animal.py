import random
import main.py 

class Animal:
    def __init__(self, legs, hand, eating_type, habitat_type,sound):
        self.legs = legs
        self.hand = hand
        self.eating_type = eating_type
        self.habitat_type = habitat_type
        self.sound = sound
    
    def make_sound(self):
        return "chosen animal sound"

class Cow(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="herbivorous", habitat_type="land",sound="cow cow")

class Monkey(Animal):
    def __init__(self):
        super().__init__(legs=2, hand=2, eating_type="omnivorous", habitat_type="land",sound= "mauru")

class Dog(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land",sound="bhau bhau")

class Cat(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land",sound="mau mau")

class Tiger(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land",sound="dhure")

class Goat(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="herbivorous", habitat_type="land",sound="bya bya")
class Bull(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="herbivorous", habitat_type="land",sound="handrulk")

class Elephant(Animal):
    def __init__(self):
        super().__init__(legs=2, hand=2, eating_type="Herbivorous", habitat_type="land",sound="hahah")

class Lion(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land",sound="bhuree")




   