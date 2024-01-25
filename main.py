user_input = input("Choose a set of animals (a, b, c): ")

animals = []
for i in range(3):
    random_animal = random.choice([Cow(), Monkey(), Dog(),Lion(),Goat(),Tiger(),Bull(),Elephant()])
    animals.append(random_animal)

for animal in animals:
    print(animal_says(animal).make_sound())
