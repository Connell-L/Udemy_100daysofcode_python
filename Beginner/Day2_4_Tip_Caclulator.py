# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

bill_total = float(input("What is the total bill? \n"))
num_of_people = int(input("How many people are there? \n"))
tip = int(input("What percentage do you want to give as a tip? \n"))
personal_bill = bill_total / num_of_people
tip_percentage = tip / 100 * personal_bill
bill_per_person = personal_bill + tip_percentage


#another way to do instead of rounding. turns it to a string that abides by the 2 decimal places rule

bill = "{:.2f}".format(bill_per_person)

print(bill)
