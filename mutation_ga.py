from mutator import Mutator
from genetic_algorithm import evolve

mutator = Mutator(2)

def replace(population):
    parent = population.select_by_tournament()
    child = mutator.reproduce_asexually(parent)
    population.replace_by_tournament(child)

evolve("Methinks it is like a weasel", replace)
