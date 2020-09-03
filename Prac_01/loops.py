"""
CP1404/CP5632 - Practical
Different Loop patterns
"""

# Example. Loop that counts in 2s from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# A. Loop that counts in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B. Loop that counts down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C. Loop that prints the amount of stars the user inputs on the same
number_of_stars = int(input("Number of stars: "))
for i in range(1, number_of_stars + 1,):
    print("*", end='')
print()

# D. Loop that prints the amount of stars the user inputs on different lines
number_of_stars = int(input("Number of stars: "))
for i in range(0, number_of_stars):
    for j in range(0, i + 1):
        print("*", end=' ')
    print()