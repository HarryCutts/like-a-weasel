from nose.tools import *

from crossover import UniformCrossover
from individual import Individual

def test_crossover():
    reproducer = UniformCrossover()
    parent_0 = Individual("abcdefghik")
    parent_1 = Individual("0123456789")
    child = reproducer.sexually_reproduce(parent_0, parent_1)
    assert_true(all(c in [a, b] for a, b, c in zip(parent_0.chars, parent_1.chars, child.chars)))
