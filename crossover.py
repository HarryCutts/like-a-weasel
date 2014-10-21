from random import random

from individual import Individual

class UniformCrossover:
    def sexually_reproduce(self, parent_0, parent_1):
        child_chars = [a if random() < 0.5 else b for a, b in zip(parent_0.chars, parent_1.chars)]
        return Individual(child_chars)

if __name__ == '__main__':
    LENGTH = 10
    reproducer = UniformCrossover()
    parent_0 = Individual(LENGTH)
    parent_1 = Individual(LENGTH)
    child = reproducer.sexually_reproduce(parent_0, parent_1)
    print("Parent 0 " + str(parent_0))
    print("Parent 1 " + str(parent_1))
    print("Child    " + str(child))
