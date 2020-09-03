"""
CP1404/CP5632 - Practical
Exceptions to complete
Program that gets an integer from the user and does not crash when a non-number is entered
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Enter a number: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)