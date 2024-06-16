rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

listOfChoices = [rock, paper, scissors]

import random

print("Welcome to Rock, Paper, Scissors Game!")
while(True):
    user_choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : ")
    )
    print("You chose :")
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    else:
        print(scissors)

    computer_choice = random.randint(0, 2)

    print("Computer chose :")
    print(listOfChoices[computer_choice])
    if user_choice == 0:
        if computer_choice == 0:
            print("It's a draw!")
        elif computer_choice == 1:
            print("You lose!")
        else:
            print("You win!")
    elif user_choice == 1:
        if computer_choice == 1:
            print("It's a draw!")
        elif computer_choice == 2:
            print("You lose!")
        else:
            print("You win!")
    else:
        if computer_choice == 2:
            print("It's a draw!")
        elif computer_choice == 1:
            print("You lose!")
        else:
            print("You win!")
