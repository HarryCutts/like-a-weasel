from nose.tools import *

from individual import Individual
from mutator import Mutator

def test_mutated_length():
    LENGTH = 10
    ind1 = Individual(LENGTH)
    mutator = Mutator(2)
    ind2 = mutator.reproduce_asexually(ind1)
    assert_true(len(ind1.chars) == len(ind2.chars))
