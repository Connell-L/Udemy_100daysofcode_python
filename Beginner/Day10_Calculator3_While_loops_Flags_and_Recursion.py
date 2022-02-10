from Day10_art import logo

# Calculator

# Add
def add(n1, n2):
	"""Adds numbers together."""
	return n1 + n2


# Subtract
def subtract(n1, n2):
	"""Subtracts one number from another."""
	return n1 - n2


# Multiply
def multiply(n1, n2):
	"""Multiplies one number by another."""
	return n1 * n2


# Divide
def divide(n1, n2):
	"""Divides one number by another."""
	return n1 / n2


operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}



def calculator():
	print(logo)
	num1 = float(input("What's the first number?: "))
	for symbols in operations:
		print(symbols)
	should_continue = True

	while should_continue:
		operation_symbol = input("Pick and operation from the line above: ")
		num2 = float(input("What's the next number?: "))
		calculation_function = operations[operation_symbol]
		answer = calculation_function(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {answer}")

		keep_going = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation: ")
		if keep_going == "y":
			num1 = answer
		else:
			should_continue = False
			calculator()

calculator()
