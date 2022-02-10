# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# https://www.askpython.com/python/string/convert-string-to-list-in-python
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences

#Write your code below this line 👇

import random

number_of_people = len(names)

# Have to put -1 to the number of items because it is off by 1.
random_choice = random.randrange(0, number_of_people - 1)
winner = names[random_choice].title()
print(random_choice)
print(f"{winner} is paying the bill.")

# Can just do random.choice.