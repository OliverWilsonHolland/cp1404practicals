"""
CP1404/CP5632 - Practical
Exceptions questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("You cannot divide by 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# Questions
# When will a ValueError occur?
# This occurs when an invalid literal for int() is entered

# When will a ZeroDivisionError occur?
# This occurs when the denominator entered is 0


# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Create a While loop for when denominator = 0

