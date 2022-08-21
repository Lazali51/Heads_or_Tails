import random

while True:
    start = input("Start?\n(y/n)> ")

    if start == "y":

        choices = ["Tails", "Heads"]
        x = random.choices(choices)

        print(x)

    elif start == "n":
        print("Goodbye!")

    break
