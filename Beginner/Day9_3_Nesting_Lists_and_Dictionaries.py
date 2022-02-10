# Nesting is like a folder inside the dictionary

# {
# 	Key: Value,
# 	Key2: Value2,
# }

# Can have a list as a value key: [list],
# Nesting Example

# {
# 	Key: [list],
# 	Key2: {Dict},
# }

capitals = {
	"France": "Paris",
	"Germany": "Berlin",
	"Scotland": "Edinburgh",
	"England": "London"
}

# Nesting a list in a Dictionary. Each key can only have 1 value but we can use a list to extend that.

travel_log = [
	{
		"country:": "France",
		"cities_visited": ["Paris", "Lille", "Dijon"],
		"total_visits": 12
	},
	{
		"country": "Scotland",
		"cities_visited": ["Edinburgh", "Glasgow", "Stirling"],
		"total_visits": 5
	}
]

print(travel_log)

# Nest a dictionary in a dictionary

# Nesting a dictionary in a List
