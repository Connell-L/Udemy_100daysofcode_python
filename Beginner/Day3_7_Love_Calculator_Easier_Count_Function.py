# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

names = name1.lower() + name2.lower()

love_1 = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love_2 = names.count("l") + names.count("o") + names.count("v") + names.count("e")
love_score = int(str(love_1) + str(love_2))

if love_score < 10 or love_score > 90:
	print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
	print(f"Your score is {love_score}, you are alright together.")
else:
	print(f"Your score is {love_score}.")

