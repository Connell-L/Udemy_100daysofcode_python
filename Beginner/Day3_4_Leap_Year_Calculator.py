year = int(input("Test a year to check if it is a leap year! \n"))

if year % 400 == 0:
	print(f"{year} is a leap year!")
elif year % 100 == 0:
	print(f"{year} is not leap year!")
elif year % 4 == 0:
	print(f"{year} is a leap year!")
else:
	print(f"{year} is a leap year!")
