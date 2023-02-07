import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = input("What do you choose? Rock, Paper or Scissors.\n ").lower()
computer = random.randint(0, 2)

if user == "rock":
    print(rock)
    if computer == 0:
        print ("Computer Choose:")
        print(rock)
        print("\nITS A DRAW!")
    elif computer == 1:
        print ("Computer Choose:")
        print(paper)
        print("\nYOU LOSE!")
    elif computer == 2:
        print ("Computer Choose:")
        print(scissors)
        print("\nYOU WIN!")
elif user == "paper":
    print(paper)
    if computer == 0:
        print ("Computer Choose:")
        print(rock)
        print("\nYOU WIN!")
    elif computer == 1:
        print ("Computer Choose:")
        print(paper)
        print("\nITS A DRAW!")
    elif computer == 2:
        print ("Computer Choose:")
        print(scissors)
        print("\nYOU LOSE!")
elif user == "scissors":
    print(scissors)
    if computer == 0:
        print ("Computer Choose:")
        print(rock)
        print("\nYOU LOSE!")
    elif computer == 1:
        print ("Computer Choose:")
        print(paper)
        print("\nYOU WIN!")
    elif computer == 2:
        print ("Computer Choose:")
        print(scissors)
        print("\nITS A DRAW!")
else:
    print("Please enter a valid input!")