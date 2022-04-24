fav_numbers = {
    "Tom": [2, 3,10],
    "Alice": [7],
    "Joshua": [9,12],
    "Jane": [12],
    "Max":[6,8]
}
for name, persons_fav_numbers in fav_numbers.items():
    if len(persons_fav_numbers) == 1:
        print(f"{name}'s favorite number is {persons_fav_numbers}\n")
    elif len(persons_fav_numbers) > 1:
        print(f"{name}'s favorite numbers are {'and '.join(str(persons_fav_numbers).strip())}\n")



"""your_fav_number = {}
numbers = input("What's your favorite number?")
your_fav_number["your favorite number"] = numbers
friends_numbers = input("What's your friend's favorite number?")
your_fav_number["your friend's number"] = friends_numbers
for person, number in your_fav_number.items():
    print(f"{person} is {number}\n")
for person in sorted(your_fav_number.keys()):
    number = your_fav_number[person]
    print(f"{person},{number}")"""