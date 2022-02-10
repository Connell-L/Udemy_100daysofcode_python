# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# bmi_height = float(height * height)
# bmi = int(weight) / bmi_height
#
# print(f"Your bmi is {bmi}")

# print(type(height))

height_num = float(height)
weight_num = float(weight)
bmi = round(weight_num / (height_num ** 2))

print(bmi)

# instead of using the 'round' function coulda just turned it into an int and it would have cut it off

# ' // ' flaw division will put it into an integer instead of juse '/' it will become a float

# /= or +=
