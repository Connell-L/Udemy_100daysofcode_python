############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random
from Day11_art import logo
import os
import os


def clear():
	os.system('clear')


# on Linux System


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def black_jack(n1):
	"""Is the score 21?"""
	if n1 == 21:
		return True


def lose(n1):
	"""Is the score over 21?"""
	if n1 > 21:
		return True


def is_ace(card_hands):
	"""Checks whether the player has drawn an ace"""
	for card in card_hands:
		if card == 11:
			return True


def blackjack():
	"""A text based blackjack game."""
	print(logo)
	play = input("Do you want to play a game of Blackjack? Type 'y' or 'no': ")
	should_continue = True
	player_hand = random.choices(cards, k=2)
	computer_hand = random.choices(cards, k=2)
	current_score = sum(player_hand)
	computer_score = sum(computer_hand)
	print(f"Your cards: {player_hand}, current score: {current_score}")
	print(f"The computer's first card is: {computer_hand[0]}")
	if play == "n":
		should_continue = False

	while should_continue:
		draw_a_card = input("Type 'y' to get another card, type 'n' to pass: ")

		# Asks to draw a card and adds a random one to player's hands
		if draw_a_card == "y":
			new_card = random.choice(cards)
			player_hand.append(new_card)
			current_score = sum(player_hand)
			print(f"Your cards: {player_hand}, current score is {current_score}")
			print(f"The computer's first card is: {computer_hand[0]}")
		if computer_score < 17:
			new_computer_card = random.choice(cards)
			computer_hand.append(new_computer_card)
			computer_score = sum(computer_hand)

		# Checks whether or not they have blackjack.
		if black_jack(current_score):
			print("You have drawn blackjack! You win!")
			should_continue = False
		elif black_jack(computer_score):
			print("The computer has drawn blackjack! You lose")

		# Checks if the scores are over 21 and if there is an ace.
		if lose(current_score) and is_ace(player_hand):
			for card in player_hand:
				if card == 11:
					player_hand[card] == 1

				if current_score > 21:
					print("You have scored over 21. You lose!")
					should_continue = False
				else:
					should_continue = True
		if lose(current_score) and not is_ace(player_hand):
			print("You have scored over 21! You lose!")
			should_continue = False
		if lose(computer_score) and is_ace(computer_hand):
			computer_score -= 10
			if computer_score > 21:
				print("The computer has scores over 21. You win!")
				should_continue = False
		if lose(computer_score) and not is_ace(computer_hand):
			print("The computer has scores over 21. You win!")
			should_continue = False

		# Checks who has the highest score
		if play == "n" or draw_a_card == "n":
			if current_score > computer_score:
				if not lose(current_score) or lose(computer_score):
					print(f"You drew {current_score} and the computer drew {computer_score}. You have won!")
					should_continue = False
			elif current_score == computer_score:
				if not lose(current_score) or lose(computer_score):
					print(f"You drew {current_score} and the computer drew {computer_score}. You draw!")
					should_continue = False
			elif computer_score > current_score:
				if not lose(current_score) or lose(computer_score):
					print(f"You drew {current_score} and the computer drew {computer_score}. You lose!")
					should_continue = False


		if not should_continue:
			play_again = input("Type 'y' to play again, or 'no' to exit.")
			if play_again == "n":
				clear()
				should_continue = False
			if play_again == "y":
				clear()
				blackjack()


blackjack()
