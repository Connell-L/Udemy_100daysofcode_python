# Functions with Outputs

# def my_function(): <----- no inputs in brackets, they are seperate.
	# result = 3 * 2 <----- saved to a variable.
	# return result <------ output of the function

# Can save the output to another variable
# output = my_function()

def format_name(f_name, l_name):
	formatted_f_name = f_name.title()
	formatted_l_name = l_name.title()
	return f"{formatted_f_name} {formatted_l_name}"
	# print(f"{formatted_f_name} {formatted_l_name}")
	# return keyword is important.
name = input("What is your name?")

format_name("angela", "ANGELA")

name_title = format_name("ANGELA, ANGELA")