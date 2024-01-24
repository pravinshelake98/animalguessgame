import random

class Animal:
    def __init__(self, legs, hand, eating_type, habitat_type):
        self.legs = legs
        self.hand = hand
        self.eating_type = eating_type
        self.habitat_type = habitat_type

class Cow(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="herbivorous", habitat_type="land")

class Monkey(Animal):
    def __init__(self):
        super().__init__(legs=2, hand=2, eating_type="omnivorous", habitat_type="land")

class Dog(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land")

class Cat(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land")

class Tiger(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land")

class Goat(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="herbivorous", habitat_type="land")
class Bull(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="herbivorous", habitat_type="land")

class Elephant(Animal):
    def __init__(self):
        super().__init__(legs=2, hand=2, eating_type="Herbivorous", habitat_type="land")

class Lion(Animal):
    def __init__(self):
        super().__init__(legs=4, hand=0, eating_type="carnivorous", habitat_type="land")




def animal_says(animal):
    if isinstance(animal, Cow):
        return "Cow says: Mowwwwwww"
    
    elif isinstance(animal, Monkey):
        return "Monkey says: Eeeee"
    
    elif isinstance(animal, Cat):
        return "Cat says: Mau Mau"
    
    elif isinstance(animal, Tiger):
        return "Tiger says: Khau khau"
    
    elif isinstance(animal, Lion):
        return "Lion says: khur khur"
    
    elif isinstance(animal, Dog):
        return "Dog says: Bhau Bhau"
    elif isinstance(animal, Goat):
        return "Goat says: Beeee"
    else:
        return "Unknown animal"
    
user_input = input("Choose a set of animals (a, b, c): ")

animals = []
for i in range(3):
    random_animal = random.choice([Cow(), Monkey(), Dog(),Lion(),Goat(),Tiger(),Bull(),Elephant()])
    animals.append(random_animal)

for animal in animals:
    print(animal_says(animal))



