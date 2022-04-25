location_1 = input("What's your favorite place?")
location_2 = input("What's your friend's favorite place?")
location_3 = input("What's your other friend's favorite place?")

favorite_places = {
    "User": location_1,
    "Jack": location_2,
    "Jeremy": location_3,
}
for name, place in favorite_places.items():
    print(f"{name}'s favorite place is {place}. ")