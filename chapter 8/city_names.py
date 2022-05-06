def format_location(city, country):
    """Creates a string containing information on where a person lives"""
    location = f"{city},{country}"
    return location


while True:
    print("This program will as you where you're from. Press q at any time to quit")
    country = input("What country do you live in? ")
    if country == "q":
        break
    city = input("Which city do you live in? ")
    if city == "q":
        break
    location = format_location(city, country)
    print(f"You are from {location}")
