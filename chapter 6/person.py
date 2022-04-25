person_1 = {"first_name": "Albert", "last_name": "Einstein", "nationality": "German"}
person_2 = {"first_name": "Marie", "last_name": "Curie", "nationality": "French"}
person_3 = {"first_name": "Stephen", "last_name": "Hawking", "nationality": "American"}
people = [person_1, person_2, person_3]
for person in people:
    first_name = person["first_name"]
    last_name = person["last_name"]
    nationality = person["nationality"]
    print(f"{first_name} {last_name} is {nationality}.")
