# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

# This gets a list indices must be integers or slices, not str error if the above 2 variables aren't made into integers.

# selected_row = map[vertical -1]
# selected_row[horizontal - 1] = "X"

# Can turn the above code into a shorter piece of code.

map[vertical - 1][horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")