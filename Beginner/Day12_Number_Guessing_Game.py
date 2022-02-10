# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = ("""\ 


 _______               ___.                    ________                            .__                   ________                       
 \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 





""")

import random

print(logo)

real_number = random.randint(0, 101)

easy = 5
hard = 10
def higher_or_lower(guess, correct_number, attempt):
	if guess == correct_number:
		return f"You got it! The answer was {real_number}."
	if guess > correct_number:
		return "Too high,"
		return "Guess again."
		return attempt -1
		return f"You have {attempt} attempts remaining to guess the number."
	if guess < real_number:
		print("Too low.")
		print("Guess again.")
		return attempt - 1
		print(f"You have {attempt} attempts remaining to guess the number.")




def number_guessing_game():
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	print(f"Pssst, the correct answer is {real_number}")
	difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
	guess = int(input("Make a guess. "))
	attempt = 0
	is_game_ended = False
	if difficulty == "easy":
		is_game_ended = False
		attempt = easy
		print(f"You have {attempt} attempts remaining to guess the number.")
		# higher_or_lower(guess, real_number, is_game_ended)
		return easy
	if difficulty == "hard":
		is_game_ended = False
		attempt = hard
		print(f"You have {attempt} attempts remaining to guess the number.")
		return hard
	while not is_game_ended:
		guess_again = int(input("Guess again. "))
		guess = guess_again
		higher_or_lower(guess, real_number, attempt)









# guess_again = int(input("Guess again. "))


number_guessing_game()
