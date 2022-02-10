def format_name(f_name, l_name):
	if f_name == "" or l_name == "":
		return "There is a missing name"
	formatted_f_name = f_name.title()
	formatted_l_name = l_name.title()
	return f"Result: {formatted_f_name} {formatted_l_name}"
	# print(f"{formatted_f_name} {formatted_l_name}")
	# return keyword is important.
	#print("This got printed")
#name = input("What is your name?")

format_name("angela", "ANGELA")

# name_title = format_name("ANGELA, ANGELA")

# can have multiple return keywords or none but things after return won't work'