# Python does not have block scope like other languages.

# new variable inside like a if block

game_level = 3
enemies = ["skeleton", "zombie", "Alien"]
if game_level < 5:
	new_enemy = enemies[0]

# if outside the if block its usuable but not inside a function. if statements don't count as local scope.

# if you create a variable inside a function it's only available there but not in if, for statements ect.