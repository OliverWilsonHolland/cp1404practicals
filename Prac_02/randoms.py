"""
CP1404/CP5632 - Practical
Random numbers practise
"""
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# On line 1 I saw a random number from 5 to 20
# The smallest number possible is 5 and the largest 20

# On line 2 I saw a random number from 3 to 10 in increments of 2
# The smallest number possible is 3 and the largest 9
# No line 2 could not produce a 4

# On line 3 I saw a random float in a range between 2.5 and 5.5
# The smallest number possible is 2.51 and the largest 5.49999999999999

# random number between 1 and 100
print(random.randint(1, 100))