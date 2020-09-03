"""
CP1404 Prac 3
refactored temperature conversion calculator
"""
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_fahrenheit(celsius):
    """calculate fahrenheit using celsius"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def calculate_celsius(fahrenheit):
    """calculate celsius using fahrenheit"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()