"""
CP1404/CP5632 Practical
emails program
"""
email_names = {}
email = str(input("Email:"))
while email != "":
    name = email.split("@")
    check = str(input("Is your name {}? (Y/n)".format(name[0].title()))).upper()
    if check == "Y":
        email_names[email] = name[0].title()
    else:
        name = str(input("Name: ")).title()
        email_names[email] = name
    email = str(input("Email:"))
for key, value in sorted(email_names.items()):
    print("{} ({})".format(value, key))
