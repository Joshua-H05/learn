cities = {
    "London": {"continent": "Europe", "population": "9 million", "language": "English"},
    "Paris": {"continent": "Europe", "population": "2.2 million", "language": "French"},
    "Melbourne": {"continent": "Oceana", "population": "5 million", "language": "English"},
}
# Print info on all 3 cities using a fstring
for city, info in cities.items():
    print(f"Here's some information about {city}: It is in {info['continent']}, "
          f"it has a population of roughly {info['population']} and the official language there is {info['language']}.")
for city, info in cities.items():
    # creates a list of all the cities by appending all the keys of the dictionaries into a list
    list_of_cities = []
    list_of_cities.append(city)
    # Asks the user for his/ her favorite city
    favorite_city = input("What is your favorite city?")
    # If the input corresponds to one ot the cities in the dictionary, information on the city is printed
    if favorite_city in list_of_cities:
        print(f"{cities[favorite_city]}")
        for city, info in cities[favorite_city]
# I would like to access the embedded dictionary with the key that corresponds to the input given by the user
# (the value in favorite_cities) so that if the user prints "Paris" for example, information on Paris is given.

