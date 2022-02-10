#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

random_word = random.choice(word_list)
word_length = len(random_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter!\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
print(random_word)
bad_guesses = []
correct_guesses = []
letter_count = random_word.count(guess)

for char in random_word:
	if guess == char:
		print(f"{guess} is correct!")
	else:
		print("This isn't correct!")



