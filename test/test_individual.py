from nose.tools import *

from individual import Individual

def test_generated_length():
    LENGTH = 10
    ind = Individual(LENGTH)
    assert_true(len(ind.chars) == LENGTH)

class TestEvaluateAgainst:
    def setup(self):
        self.individual_a = Individual('0123456789')

    def test_identical(self):
        chars = self.individual_a.chars
        assert_true(self.individual_a.evaluate_against(chars) == len(chars))

    def test_no_similarity(self):
        assert_true(self.individual_a.evaluate_against('a tallship') == 0)
