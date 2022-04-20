fav_numbers = {
    "Tom": 2,
    "Alice": 7,
    "Joshua": 9,
    "Jane": 12,
    "Max": 6
}
for name, number in fav_numbers.items():
    print(f"{name}'s favorite number is {number}\n")
for number in fav_numbers.values():
    print (number)

your_fav_number = {}
numbers = input("What's your favorite number?")
your_fav_number["your favorite number"] = numbers
friends_numbers = input("What's your friend's favorite number?")
your_fav_number["your friend's number"] = friends_numbers
for person, number in your_fav_number.items():
    print(f"{person} is {number}\n")
for person in sorted(your_fav_number.keys()):
    number = your_fav_number[person]
    print(f"{person},{number}")