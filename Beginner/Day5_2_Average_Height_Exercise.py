# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
for heights in student_heights:
  total_height += heights

print(total_height)

number_of_heights = 0
for number in student_heights:
  number_of_heights += 1

print(number_of_heights)

average_height = total_height / number_of_heights
print(round(average_height))

