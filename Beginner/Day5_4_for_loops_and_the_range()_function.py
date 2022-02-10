# for loops don't always use lists.
# using for loops with the range() function
# for number in range(a, b):
	#print(number)

#starts from 0 so if you want all 1-10 you'd have to go 1-11.
# range() function is range(start, stop, step) where the step is how large the steps between them are like every 3rd number
total = 0
for number in range(1, 101):
	total += number
print(total)