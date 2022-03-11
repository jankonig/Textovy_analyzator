#texts
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


oddelovac = "-" * 40
H = 0
lower = 0
title = 0
upper = 0
number = 0
soucet = []
slovnikslov = {}

# login
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

volba_textu = ["1", "2", "3"]

username = input("Username: ")

if username in users:
    password = input("Password: ")
    if users[username] == password:
        print(oddelovac)
        print("Welcome to the application,", username, "\nWe have 3 texts to be analyzed.")
        print(oddelovac)
        user_input = input("Enter number between 1 and 3: ")
        print(oddelovac)

        if user_input in volba_textu:
            print("There are", len(TEXTS[int(user_input) - 1].split()), "in the selected text.")

            for x in TEXTS[int(user_input) - 1].split():
                if x.istitle():
                    title = title + 1
            print("There are", title, "titlecase words.")

            for x in TEXTS[int(user_input) - 1].split():
                if x.isupper() and x.isalpha():
                    upper = upper + 1
            print("There are", upper, "uppercase words.")

            for x in TEXTS[int(user_input) - 1].split():
                if x.islower():
                    lower = lower + 1
            print("There are", lower, "lowercase words.")

            for x in TEXTS[int(user_input) - 1].split():
                if x.isdigit():
                    number = number + 1
            print("There are", number, "numeric strings.")

            for x in TEXTS[int(user_input) - 1].split():
                if x.isdigit():
                    soucet.append(int(x))
            print("The sum of all the numbers", sum(soucet))

            slovo2 = TEXTS[int(user_input) - 1].replace(",", "").replace(".", "")
            slovo2 = [len(i) for i in slovo2.split()]

            for i in slovo2:
                slovnikslov[i] = slovnikslov.get(i, 0) + 1

            print(oddelovac)
            print("{:<3} {:<1} {:<20} {:<1} {:<15}".format("LEN", "|", "OCCURRENCES", "|", "NR."))
            print(oddelovac)

            for key, value in sorted(set(slovnikslov.items())):
                print("{:<3} {:<1} {:<20} {:<1} {:<15}".format(str(key).rjust(3, " "), "|",
                                                                str(value * "*").ljust(20, " "), "|",
                                                                str(value).ljust(15, " ")))

        else:
            print("Option is not in the list")

    else:
        print("Wrong password.")
else:
    print("Unregistered user, terminating the program...")