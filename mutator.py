from random import random

from individual import Individual

class Mutator:
	"""
	Mutates Individuals according to certain parameters.
	"""

	def __init__(self, num_mutations):
		"""
		Creates a new Mutator with the given settings.

		:param num_mutations: the average number of mutations to make each time.
		"""
		self.num_mutations = num_mutations

	def reproduce_asexually(self, individual):
		"""
		Creates a copy of an individual, probably with mutations applied.
		"""
		child = list(individual.chars)
		for key, char in enumerate(individual.chars):
			if random() < (self.num_mutations / len(individual.chars)):
				child[key] = individual.rand_chr()

		return Individual(child)


if __name__ == '__main__':
	ind = Individual("This isn't Shakespeare.")
	print("Start\t", ind)
	mutator = Mutator(3)
	for i in range(10):
		ind = mutator.reproduce_asexually(ind)
		print(i, ind)
