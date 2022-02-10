travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, times_visited, countries_visited):
    # travel_log.extend({"country": country, "visits": times_visited, "cities": countries_visited})
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = times_visited
  new_country["cities"] = countries_visited
  travel_log.append(new_country)





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)




