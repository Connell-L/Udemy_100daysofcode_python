# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

row1_1 = "11"
row1_2 = "21"
row1_3 = "31"
row2_1 = "12"
row2_2 = "22"
row2_3 = "23"
row3_1 = "31"
row3_2 = "32"
row3_3 = "33"

if position == row1_1:
	row1[0] = "X"
elif position == row1_2:
	row1[1] = "X"
elif position == row1_3:
	row1[2] = "X"
elif position == row2_1:
	row2[0] = "X"
elif position == row2_2:
	row1[1] = "X"
elif position == row2_3:
	row1[2] = "X"
elif position == row3_1:
	row1[0] = "X"
elif position == row2_2:
	row1[1] = "X"
elif position == row2_3:
	row1[2] = "X"
else:
	print("Error. Try again!")

print(f"{row1}\n{row2}\n{row3}")
