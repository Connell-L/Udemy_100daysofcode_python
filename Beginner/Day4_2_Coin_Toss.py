import random

heads_or_tails = input("Heads or Tails?\n").lower()
if heads_or_tails == "heads":
	coin_toss = random.randint(0, 1)
	if coin_toss == 0:
		print("Heads! You win!")
	else:
		print("Heads! You lose!")
if heads_or_tails == "tails":
	coin_toss = random.randint(0, 1)
	if coin_toss == 1:
		print("Tails! You win!")
	else:
		print("Tails! You lose!")

print(coin_toss)