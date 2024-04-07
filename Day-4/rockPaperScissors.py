import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
Rock
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
Paper
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
Scissors
'''

print("Welcome to Rock-Papers-Scissors game")
inp = int(input("0 => Rock, 1 => Paper, 2 => Scissors: "))

guess_list = ["R", "P", "S"]
num = random.randint(0, len(guess_list)-1)

guessed = guess_list[num]

print("You Choosed: ")
if inp == 0:
    print(rock)
    print()
    print("Computer choosed: ")
    if guessed == "P":
        print(paper)
        print("You Loose")
    elif guessed == "S":
        print(scissors)
        print("You Won")
    else:
        print(rock)
        print("It's a Tie")

elif inp == 1:
    print(paper)
    print()
    print("Computer choosed: ")
    if guessed == "P":
        print(paper)
        print("It's a Tie")
    elif guessed == "S":
        print(scissors)
        print("You Loose")
    else:
        print(rock)
        print("You Won")

elif inp == 2:
    print(scissors)
    print()
    print("Computer choosed: ")
    if guessed == "P":
        print(paper)
        print("You Won")
    elif guessed == "S":
        print(scissors)
        print("It's a tie")
    else:
        print(rock)
        print("You Loose")

else:
    print("Invalid Input.")