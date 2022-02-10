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
import random

game_list = [rock, paper, scissors]
user_choice = input("Rock, Paper or Scissors\n").lower()
random_choice = random.choice(game_list)

if user_choice == "rock":
	print("You picked Rock!")
	print(game_list[0])
	if random_choice == game_list[0]:
		print("Rock! You draw!")
		print(game_list[0])
	elif random_choice == game_list[1]:
		print("Paper! You win!")
		print(game_list[1])
	elif random_choice == game_list[2]:
		print("Scissors! You lose!")
		print(game_list[2])
	else:
		print("Error: Please pick Rock, Paper or Scissors")

if user_choice == "paper":
	print("You picked Paper!")
	print(game_list[1])
	if random_choice == game_list[0]:
		print("Rock! You win")
		print(game_list[0])
	elif random_choice == game_list[1]:
		print("Paper! You draw!")
		print(game_list[1])
	elif random_choice == game_list[2]:
		print("Scissors! You lose!")
		print(game_list[2])
	else:
		print("Error: Please pick Rock, Paper or Scissors")

if user_choice == "scissors":
	print("You picked Scissors!")
	print(game_list[2])
	if random_choice == game_list[0]:
		print("Rock! You lose!")
		print(game_list[0])
	elif random_choice == game_list[1]:
		print("Paper! You win!")
		print(game_list[1])
	elif random_choice == game_list[2]:
		print("Scissors! You draw!")
		print(game_list[2])
	else:
		print("Error: Please pick Rock, Paper or Scissors")