class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# add another cat
class Didi(Cat):
    def sing(self, sounds):
        return (f'{sounds}')


# Create a list of all of the pets (create 3 cat instances from the above)
simon = Simon('Simon', 2)
sally = Sally('Sally', 3)
didi = Didi('Didi', 13)

my_cats = [simon, sally, didi]

# Instantiate the Pet class with all your cats. use variable my_pets

my_pets = Pets(my_cats)

# Output all of the cats walking using the my_pets instance
for pet in my_pets.animals:
    print(pet.walk())

# the clean answer is just my_pets.walk(), because otherwise
# I'm repeating the walk method...
# oh well, this was my solution either ways. you live you learn I guess...
