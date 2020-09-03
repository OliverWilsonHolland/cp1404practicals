"""
CP1404 Prac 3
refactored password checker

"""
MIN_LENGTH = 4


def main():
    password = get_password()
    display_password(password)


def display_password(password):
    """display password as asterisks"""
    print("*" * len(password))


def get_password():
    """validate length of password"""
    password = input("Enter Password: ")
    while len(password) < MIN_LENGTH:
        print("Invalid password")
        password = input("Enter Password: ")
    return password


main()