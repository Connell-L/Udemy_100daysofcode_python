# Using the for loop range() function with step size. Could have started with 2 not 0.

total = 0
for number in range(0, 101, 2):
	total += number
print(total)

# Could have used the modulo.

total2 = 0
for number in range(1, 101):
	if number % 2 == 0:
		total2 += number
print(total2)
