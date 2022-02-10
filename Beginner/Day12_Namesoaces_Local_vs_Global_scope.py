################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
  potion_strength = 2
  print(potion_strength)

# ^^ This will run because it's inside the function

drink_potion()
#print(potion_strength)

# ^^ This won't compile because it can't be used outside the function.

# If we want to access something outside a function we have to create them outside functions
# if inside functions we can define it as global
# namespace - we defined stuff and that namespace is valid in certain scopes