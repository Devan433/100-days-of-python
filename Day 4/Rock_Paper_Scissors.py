import random
print("Welcome to Rock, Paper, Scissors!")
player = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))
computer = random.randint(0, 2)
if player == 0:
    print("You chose Rock")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif player == 1:
    print("You chose Paper")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif player == 2:
    print("You chose Scissors")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
else:
    print("Invalid choice! You lose.")
    exit()

print("Computer chose:")
if computer == 0:
    print("Rock")
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer == 1:
    print("Paper")
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
else:
    print("Scissors")
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if player == computer:
    print("It's a draw!")
elif (player == 0 and computer == 2) or \
     (player == 1 and computer == 0) or \
     (player == 2 and computer == 1):
    print("You win!")
else:
    print("You lose!")
