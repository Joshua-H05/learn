cities = {
    "London": {"continent": "Europe", "population": "9 million", "language": "English"},
    "Paris": {"continent": "Europe", "population": "2.2 million", "language": "French"},
    "Melbourne": {"continent": "Oceana", "population": "5 million", "language": "English"},
}
for city, info in cities.items():
    print(f"Here's some information about {city}: It is in {info['continent']}, "
          f"it has a population of roughly {info['population']} and the official language there is {info['language']}.")
