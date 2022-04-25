# Dictionary nested in another dictionary: The main dictionary uses cities as keys and information on them as values
# The nested dictionaries use types of info as keys and the info as values
cities = {
    "London": {"continent": "Europe", "population": "9 million", "language": "English"},
    "Paris": {"continent": "Europe", "population": "2.2 million", "language": "French"},
    "Melbourne": {"continent": "Oceana", "population": "5 million", "language": "English"},
}
# iterates around each city in the main dictionary and prints information on them using the nested dictionaries
for city, info in cities.items():
    print(f"Here's some information about {city}: It is in {info['continent']}, "
          f"it has a population of roughly {info['population']} and the official language there is {info['language']}.")
# An empty list of cities
list_of_cities = []
# Iterates around the keys in the main dictionary, taking each key and appending it into the list of cities
for city in cities.keys():
    list_of_cities.append(city)
print(list_of_cities)
# Asks the user for his/ her favorite city
favorite_city = input("What is your favorite city?").title()
# Checks if the user's favorite city is in the list of cities/ in the dictionary
# If it is, information on the city is printed. If not, the program lets the user know
if favorite_city in list_of_cities:
    # Adding the .title() function to favorite_city here doesn't work because it only capitalizes the value of the
    # variable in this line.
    # This isn't enough because the variable needs to be capitalized at all times as it is needed to access values later
    # in lines 28-30
    print(f"Here is some information on {favorite_city}: "
            f"It is in {cities[favorite_city]['continent']}, "
            f"It has a population of {cities[favorite_city]['population']}"
            f" and its official language is {cities[favorite_city]['language']} ")
elif favorite_city not in list_of_cities:
    print(f"Sorry, {favorite_city} is not in our database.")
