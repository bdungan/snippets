# Adapted from 100 days of Code by Angela Yu
# Rock, Paper, Scissors game

# import random and time modules from standard python library
import random
import time

# String Block begins and ends with 3 single quotes
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

# Create list of ascii art defined above for printing later
choices = [rock, paper, scissors]
# Create list of synonymous string values for printing later
choices_str = ["Rock", "Paper", "Scissors"]

# Ask user for their input
choice = input("Please choose from the following:"
      '''
  1) Rock
  2) Paper
  3) Scissors
  :''')

# Check and normalize input (try block was not in this lesson)
try:
    # check to see if the user input the number or spelled out the selection
    choice_idx = int(choice) - 1
except ValueError:
    # user may have entered the string
    if choice.lower() == "rock":
        choice_idx = 0
    elif choice.lower() == "paper":
        choice_idx = 1
    elif choice.lower() == "scissors":
        choice_idx = 2
    else:
        print("The value entered is not a valid choice")
        exit(1)

if choice_idx < 0 or choice_idx > 2:
    print("The value entered is not a valid choice")
    exit(1)

rand_idx = random.randint(0,2)

print("Rock...")
# this is where time is being used to delay output (not in this lesson)
time.sleep(.35)
print("Paper...")
time.sleep(.35)
print("Scissors...")
time.sleep(.35)
print("Shoot!")
print(f"You chose: {choices_str[choice_idx]} \n {choices[choice_idx]}")
print(f"Opponent chose: {choices_str[rand_idx]} \n {choices[rand_idx]}")

win = 1
if choice_idx == rand_idx:
    print("It's a draw")
    exit(0)
elif choice_idx == 0 and rand_idx == 1:
    win = 0
elif choice_idx == 0 and rand_idx == 2:
    win = 1
elif choice_idx == 1 and rand_idx == 0:
    win = 1
elif choice_idx == 1 and rand_idx == 2:
    win = 0
elif choice_idx == 2 and rand_idx == 0:
    win = 0
elif choice_idx == 2 and rand_idx == 1:
    win = 1

if win == 1:
    print("You win! :)")
else:
    print("You lose :(")