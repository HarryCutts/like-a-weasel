from random import randint

from population import Population

def evolve(target, replace):
    replacements = 0

    population = Population(500, target)
    while population.max_fitness() < len(target):
        replace(population)
        replacements = replacements + 1

    print("After",replacements,"replacements, the best individual is \"" +
          str(population.best_individual()) + "\".")
