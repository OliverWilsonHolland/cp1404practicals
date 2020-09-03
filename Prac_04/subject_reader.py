"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    names = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        names.append(parts)
    return names
    input_file.close()


def display_data(data):
    for i in range(0, len(data)):
        names_data = data[i]
        print("{} is taught by {} and has {:2} students".format(names_data[0], names_data[1], names_data[2]))


main()