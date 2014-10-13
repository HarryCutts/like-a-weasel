from random import randint

from individual import Individual

class Population:
    def __init__(self, size, target):
        self.target = target
        self._population = [Individual(len(target)) for i in range(size)]
        self._best_individual = max(self._population, key=lambda i: i.evaluate_against(target))
        self._max_fitness = self._best_individual.evaluate_against(target)

    def choose_random(self):
        return self._population[randint(0, len(self._population) - 1)]

    def select_by_tournament(self):
        a = self.choose_random()
        b = self.choose_random()
        return a if a.evaluate_against(self.target) > b.evaluate_against(self.target) else b

    def replace_by_tournament(self, new_individual):
        a = self.choose_random()
        b = self.choose_random()
        replaced = a if a.evaluate_against(self.target) < b.evaluate_against(self.target) else b
        self._population.remove(replaced)
        self._population.append(new_individual)

        new_fitness = new_individual.evaluate_against(self.target)
        if new_fitness > self._max_fitness:
            self._max_fitness = new_fitness
            self._best_individual = new_individual

    def max_fitness(self):
        return self._max_fitness

    def best_individual(self):
        return self._best_individual
