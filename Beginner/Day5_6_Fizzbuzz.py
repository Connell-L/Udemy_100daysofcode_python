for number in range(1, 101):
	if number % 3 == 0 and number % 5 == 0:
		number = "Fizzbuzz"
	elif number % 3 == 0:
		number = "Fizz"
	elif number % 5 == 0:
		number = "Buzz"
	print(number)

# elif statements will stop as soon as they find a statement that is true so have to put fizzbuzz at the top.
# could have done print statements and not changing the data.