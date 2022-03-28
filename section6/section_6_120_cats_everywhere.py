class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat('fabian', 2)
cat2 = Cat('Didi', 13)
cat3 = Cat('Pinóquio', 7)


# 2 Create a function that finds the oldest cat
def oldest_cat(*ages):
    return max(ages)


print(
    f'The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.')
