"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in
                 full_names]
print(full_initials)

# one more example, using filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# TODO: use a list comprehension to create a list of all of the full_names
lower_full_names = []
for i in range(0, len(full_names)):
    lower_full_name = ""
    lower_full_name = full_names[i].lower()
    lower_full_names.append(lower_full_name)
print(lower_full_names)

almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
# TODO: use a list comprehension to create a list of integers
numbers = []
for i in range(0, len(almost_numbers)):
    number = int(almost_numbers[i])
    numbers.append(number)
print(sum(numbers))

# TODO: use a list comprehension to create a list of only the numbers that are
greater_numbers = []
for i in range(0, len(numbers)):
    number = numbers[i]
    if number > 9:
        greater_numbers.append(number)
print(greater_numbers)