# Functions with more than 1 input

name_input = input("What is your name?\n").title()
location_input = input("Where do you live?\n").title()

def greet_with(name, location):
	print(f"Hello {name}!")
	print(f"How is the weather in {location}?")

greet_with(name_input, location_input)

# Order of data has to match when defining the function and when calling it.
# Positional Arguments
# def my_function(a, b, c):
	# Do this with a
	# Then do this with b
	# FInally do this with c

# a = 3
# b = 1
# c = 2

# my_function(3, 1, 2)

# Check positioning of arguments with parameters.

# Keyword Arguments

# my_function(a=1, b=2, c=3)
# Order doesn't matter in keyword arguments.