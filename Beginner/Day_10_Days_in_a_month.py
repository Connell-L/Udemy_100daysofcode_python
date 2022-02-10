def is_leap(years):
	if years % 4 == 0:
		if years % 100 == 0:
			if years % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False

def days_in_month(year_input, month_input):
	month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	#leap_or_not = is_leap(year_input)
	if is_leap(year_input) and month == 2:
		return 29
	else:
		which_month = month_days[month_input - 1]
		return which_month


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












