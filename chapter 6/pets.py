pets = {
    "tom": {"species": "cat", "owner": "James", "age": 3},
    "jerry": {"species": "hamster", "owner": "Max", "age": 1},
    "victor": {"species": "dog", "owner": "lily", "age": 5},
}

for person, pet in pets.items():
    print(f"{person} is a {pet['species']}. His owner is {pet['owner']} and he is {pet['age']}")
# advantage of using dictionaries: Easier to access the information stored


