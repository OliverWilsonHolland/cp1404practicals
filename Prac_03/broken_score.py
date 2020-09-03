"""
CP1404 Prac 3
refactored broken score program
"""
import random


def main():
    score = get_score()
    if score >= 50 and score >= 90:
        print("Passable")
    elif score > 90:
         print("Excellent")
    else:
        print("Bad")
    print("Random score", random.randint(0, 100))


def get_score():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        return score


main()