"""
CP1404/CP5632 Practical
Quick Picks
"""

import random
number_picks = int(input("How many quick picks? "))
for i in range(0, number_picks):
    picks = []
    for i in range(0, 6):
        pick = random.randint(0, 45)
        while pick in picks:
            pick = random.randint(0, 45)
        picks.append(pick)
    picks.sort()
    print("{:2} {:2} {:2} {:2} {:2} {:2}".format(picks[0], picks[1], picks[2], picks[3], picks[4], picks[5]))