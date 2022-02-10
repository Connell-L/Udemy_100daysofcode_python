student_scores = {
	"Harry": 81,
	"Ron": 78,
	"Hermione": 99,
	"Draco": 74,
	"Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

student_grades = {}


# TODO-2: Write your code below to add the grades to student_grades.👇
# key could have been anything. it would always refer to the dictionary key.
for key in student_scores:
	# Could have saved text and made a variable.
	# key = student_scores[key]
	if student_scores[key] <= 70:
		student_grades[key] = "Fail"
	elif student_scores[key] >= 71 and student_scores[key] <= 80:
		student_grades[key] = "Acceptable"
	elif student_scores[key] >= 81 and student_scores[key]  <= 90:
		student_grades[key] = "Exceeds Expectations"
	else:
		student_grades[key] = "Outstanding"




	# 🚨 Don't change the code below 👇
print(student_grades)





