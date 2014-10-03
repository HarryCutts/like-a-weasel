from random import randint

class Individual:
    """Represents an individual in the population."""

    def __init__(self, string):
        """Creates a new random individual with the specified length."""
        if type(string) == int:
            self.chars = [self.rand_chr() for i in range(string)]
        elif type(string) == str:
            self.chars = list(string)
        else:
            self.chars = string

    def rand_chr(self):
        """Returns a random character from the set of valid characters."""
        return chr(randint(32, 126))

    def evaluate_against(self, target):
        """
        Returns the number of characters of the individual which match those in
        the given target string.
        """
        matches = [a == b for a, b in zip(self.chars, list(target))]
        return matches.count(True)

    def __str__(self):
        return ''.join(self.chars)


if __name__=='__main__':
    target = "Methinks it is like a weasel"
    print(target, len(target))
    for i in range(10):
        ind = Individual(len(target))
        print(ind, ind.evaluate_against(target))
