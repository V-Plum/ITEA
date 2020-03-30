import random

class Country:
    def __init__(self, population, name, area):
        self.population = population
        self.name = name
        self.area = area

    def calc_population(self, quantity):
        plus_minus = 1 if random.random() < 0.5 else -1
        population_difference = plus_minus * quantity
        self.population = self.population + population_difference

ukraine = Country(40000000, "Ukraine", 603628)
quantity = random.randrange(1000, 10000, 2)
ukraine.calc_population(quantity)
print(ukraine.population)