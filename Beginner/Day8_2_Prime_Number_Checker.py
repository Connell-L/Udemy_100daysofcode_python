# Write your code below this line 👇
prime_number == False
def prime_checker(number):
	for i in range(1, 101):
		if number % number == 0 and not (number % i) == 0:
			prime_number == True
		else:
			prime_number == False

if prime_number  == True:
	print(f'{n} is a prime number!')
else:
	print(f"{n} is not a prime number!")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
