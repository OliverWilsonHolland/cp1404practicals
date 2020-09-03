"""
CP1404/CP5632 - Practical
files practice
write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it
write code that reads their name from "name.txt" and prints it

"""

# Part 1
out_file = open("name.txt", 'w')
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# Part 2
in_file = open("name.txt", 'r')
print("Your name is", in_file.read())
in_file.close()

# Part 3
out_file = open("numbers.txt", 'w')
print(17, file=out_file)
print(42, file=out_file)
print(400, file=out_file)
out_file.close()

# Program that just sums the first two lines
in_file = open("numbers.txt", 'r')
total = 0
for i in range(0, 2):
    number = in_file.readline()
    total += int(number)
print(total)
in_file.close()


# Program that sums any amount of lines
in_file = open("numbers.txt", 'r')
lines = 3
total = 0
for i in range(0, lines):
    number = in_file.readline()
    total += int(number)
print(total)
in_file.close()
# This is not correct but it does work!