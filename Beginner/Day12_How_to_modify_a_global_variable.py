# Modifying Global Scope

enemies = "Skeleton"

def increase_enemies():
	enemies = "Zombies"
	print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Bad idea to call global and local variables the same name.
# Referenced before assignment which thinks you are trying to tapping into a local variable without permissions.
# We have to explicitly say 'global' variable inside functions and is what we want to use.
# Downsides of modifying globals inside functions is error prone. Tapping into and using it is good.
# How to do with modifying?
# instead of modifying globals we can use it to return 