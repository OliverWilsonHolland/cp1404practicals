"""CP1404/CP5632 Practical - guitar class test."""

from Prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 16035.40)
print("{} get_age() expected 98. Got {}".format(gibson.name, gibson.get_age()))
print("{} get_age() expected 7. Got {}".format(another_guitar.name, another_guitar.get_age()))
print("{} is_vintage() expected True. Got {}".format(gibson.name, gibson.is_vintage()))
print("{} is_vintage() expected False. Got {}".format(another_guitar.name, another_guitar.is_vintage()))