"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Still need to brush up on what structures to use where I think this is the most efficient
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("Invalid score")
elif score >= 50:
    if score > 90:
        print("Excellent")
    else:
        print("Passable")
else:
    print("Bad")