from individual import Individual
from mutator import Mutator

num_tries = 0
num_moves = 0

TARGET = "Methinks it is like a weasel"
mutator = Mutator(2)
ind = Individual(len(TARGET))
fitness = ind.evaluate_against(TARGET)
while fitness < len(TARGET):
	new_ind = mutator.reproduce_asexually(ind)
	new_fitness = new_ind.evaluate_against(TARGET)
	num_tries = num_tries + 1
	if new_fitness > fitness:
		ind = new_ind
		fitness = new_fitness
		num_moves = num_moves + 1
		print(new_ind)

print("Found in",num_tries,"tries and",num_moves,"moves.")
