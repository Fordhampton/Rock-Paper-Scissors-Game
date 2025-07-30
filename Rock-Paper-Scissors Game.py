# Rock-Paper-Scissors Game

import random

print("==Rock-Paper-Scissors Game==")
name = input("Enter name: ").upper()
age = int(input("Enter age: "))
option = ["rock", "paper", "Scissor"]

while True:

    user = input("Enter rock, paper, or scissor(or quit): ").lower()

    if user == "quit":
        break

    if user not in option:
        print("Invalid input")
        continue

    comp = random.choice(option)
    print(f"Computer choice:, {comp}")

    if user == comp:
        print("It's a tie 🤗!!")

    elif (user == "rock" and comp == "scissor") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissor" and comp == "paper"):

        print(f"You win {name}")

    else:
        print(f"You lose {name}")
