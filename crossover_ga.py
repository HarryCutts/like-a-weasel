from random import randint

from mutator import Mutator
from crossover import UniformCrossover
from population import Population
from genetic_algorithm import evolve

mutator = Mutator(2)
reproducer = UniformCrossover()

def replace(population):
    parent_0 = population.select_by_tournament()
    parent_1 = population.select_by_tournament()
    result_of_crossover = reproducer.sexually_reproduce(parent_0, parent_1)
    child = mutator.reproduce_asexually(result_of_crossover)
    population.replace_by_tournament(child)

evolve("Methinks it is like a weasel", replace)
