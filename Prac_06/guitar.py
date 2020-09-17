"""CP1404/CP5632 Practical - guitar class."""


class Guitar:
    def __init__(self, name=" ", year=0, cost=0):
        """Initialise programming language."""
        self.name = name
        self.cost = cost
        self.year = year

    def __str__(self):
        return "{} ({}): $ {:.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2020 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
