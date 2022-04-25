cities = {
    "London": {"continent": "Europe", "population": "9 million", "language": "English"},
    "Paris": {"continent": "Europe", "population": "2.2 million", "language": "French"},
    "Melbourne": {"continent": "Oceana", "population": "5 million", "language": "English"},
}
# Print info on all 3 cities using a fstring
for city, info in cities.items():
    print(f"Here's some information about {city}: It is in {info['continent']}, "
          f"it has a population of roughly {info['population']} and the official language there is {info['language']}.")
    # creates a list of all the cities by appending all the keys of the dictionaries into a list
list_of_cities = []
for city in cities.keys():
    list_of_cities.append(city)
print(f"{list_of_cities}")
# Asks the user for his/ her favorite city
favorite_city = input("What is your favorite city?")

if favorite_city in list_of_cities:
    print(f"Here is some information on {favorite_city}: "
            f"It is in {cities[favorite_city]['continent']}, "
            f"It has a population of {cities[favorite_city]['population']}"
            f" and its official language is {cities[favorite_city]['language']} ")
elif favorite_city not in list_of_cities:
    print(f"Sorry, {favorite_city} is not in our database.")
