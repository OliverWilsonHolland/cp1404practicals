"""CP1404/CP5632 Practical - guitars program."""

from Prac_06.guitar import Guitar
guitars = []
print("My guitars!")
name = str(input("Name: "))
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print("{}, ({}): ${:.2f} added".format(name, year, cost))
    name = input("Name: ")
print("These are my guitars:")
for i in range(0, len(guitars)):
    vintage = ""
    if guitars[i].is_vintage() == True:
        vintage = "(vintage)"
    print("Guitar {}: {} ({}), worth ${:10,.2f}{}".format(i + 1, guitars[i].name, guitars[i].year,
                                                          guitars[i].cost, vintage))