#Exercise: Roll the die
# Randomly roll a (x)-sided die of your chosing (it doesn't have to be six).
# The program should print what side it lands on. 
# It should then ask you if you’d like to roll again.

import random

roll = True
repeat = False
confirm = ["yes", "y", "sure", "ok", "yup"]
deny = ["no", "n", "nope"]

while roll and not repeat:
    action = input("Roll the dice? [Y]es or [N]o ").lower().strip()
    if action in confirm:
        max = int(input("How many sided die do you want to roll? "))
        die = random.randint(1, max)
        print(f"You rolled a {die}!")

        again = input("How about another roll? ")
        if again in confirm:
            repeat = True
            break
        if again in deny:
            roll = False
            print("Alright then. See ya.")

while repeat:
    max = input("What sided die? ")
    max = int(max)
    die = random.randint(1, max)
    print(f"You rolled a {die}!")
    action = input("How about another? ").lower().strip()
    if action in confirm:
        repeat = True
    if action in deny:
        print("Ok. Take care.")
        break
