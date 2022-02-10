# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
	print("Hi!")
	print("What is the weather like?")
	print("How was your day?")


greet()

# Modify parts inside the function so it will change each time it is called.
# Variables can be added or 'passed' through the function by adding the data inside the parentheses.
# Create a function that allows for input.

name_input = input("What is your name \n")

def greet_with_name(name):
	print(f"Hello {name}!")
	print(f"How do you do {name}?")

greet_with_name(name_input)

# Setting parameters --> the variable inside the parentheses. Name of data.
# The argument is the actual piece of data being called with the function.  Actual data.

