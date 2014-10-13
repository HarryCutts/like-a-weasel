from random import randint

from mutator import Mutator
from population import Population

TARGET = "Methinks it is like a weasel"

replacements = 0

mutator = Mutator(2)
population = Population(500, TARGET)
while population.max_fitness() < len(TARGET):
    parent = population.select_by_tournament()
    child = mutator.reproduce_asexually(parent)
    population.replace_by_tournament(child)

    replacements = replacements + 1

print("After",replacements,"replacements, the best individual is \"" +
      str(population.best_individual()) + "\".")
