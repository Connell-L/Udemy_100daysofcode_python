# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# love_calculator_1 = 0
# if name1 = "t":
# print(f"Your love score is {love_calculator_1}{love_calculator_2}")

name1_letter_list = list(name1.lower())
name2_letter_list = list(name2.lower())
name_list = [name1_letter_list + name2_letter_list]

print(name_list)

love_calculator_1 = 0
for name in name_list:
	for char in name:
		if char == "t":
			love_calculator_1 = love_calculator_1 + 1
	for char in name:
		if char == "r":
			love_calculator_1 = love_calculator_1 + 1
	for char in name:
		if char == "u":
			love_calculator_1 = love_calculator_1 + 1
	for char in name:
		if char == "e":
			love_calculator_1 = love_calculator_1 + 1

# print(love_calculator_1)

love_calculator_2 = 0
for name in name_list:
	for char in name:
		if char == "l":
			love_calculator_2 = love_calculator_2 + 1
	for char in name:
		if char == "o":
			love_calculator_2 = love_calculator_2 + 1
	for char in name:
		if char == "v":
			love_calculator_2 = love_calculator_2 + 1
	for char in name:
		if char == "e":
			love_calculator_2 = love_calculator_2 + 1

if love_calculator_1 < 1 or love_calculator_1 > 9:
	print(f"Your score is {love_calculator_1}{love_calculator_2}, you go together like coke and mentos.")
elif 4 <= love_calculator_1 <= 5:
	print(f"Your score is {love_calculator_1}{love_calculator_2}, you are alright together.")
else:
	print(f"Your score is {love_calculator_1}{love_calculator_2}.")







