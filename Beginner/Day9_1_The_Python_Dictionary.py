# Key ------> Value
# Bug -----> An error in a program that prevents the program from running as expected
# Function -------> A piece of code that you can easily call over and over again
# Loop ----------> The action of doing something over and over again

# Examples of dictionary stuff
# {Key: Value} <--------- content of a dictionary
# {"Bug": An error in a program that prevents the program from running as expected}

# More than one dictionary entry is serperated by a comma

programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.",
	"Function": "A piece of code that you can easily call over and over again.",
}

# Dictionaries have similar syntax to lists but their elements are identified by their Key
# How to retrieve item from dictionary.

# print(programming_dictionary["Bug"])

# Key errors are usually typos.

# Adding new items to dictionary.

programming_dictionary["Loop"] = "The action of doing something over and over again"
print(programming_dictionary)

# Creating an empty dictionary. Then add to it using the above methods.
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Useful to do stuff like clear a user's progress.

# Edit an item in a dictionary. Will assign what you put.
programming_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
# for thing in programming_dictionary:
# 	print(thing)

# ^ Just gives the Key.
for key in programming_dictionary:
	print(key)
	# Value is printing with the line below.
	print(programming_dictionary[key])





