fav_numbers = {
    "Tom": [2, 3, 10],
    "Alice": [7],
    "Joshua": [9, 12],
    "Jane": [12],
    "Max": [6, 8]
}

for name, persons_fav_numbers in fav_numbers.items():
    if len(persons_fav_numbers) == 1:
        print(f"{name}'s favorite number is {persons_fav_numbers[0]}\n")
    elif len(persons_fav_numbers) > 1:
        """print(f"{name}'s favorite numbers are {'and '.join(str(persons_fav_numbers).strip())}\n")"""
        # problem: join takes a list, but the code converts it to a string--> messes up the join function
        # lines 14- 17: imperative programming--> spell out steps--> tell computer how to do something
        # list comprehension: declarative programming--> tell computer what you want, leave process up to computer
        fav_numbers_string = []
        for number in persons_fav_numbers:
            fav_numbers_string.append(str(number))
        print(f"{name}'s favorite numbers are {' and '.join(fav_numbers_string)}")
        # list comprehension: completes lines 14-17 all in one line-->
        # essentially: for every number in persons_fav_numbers: turn into a string--> everything is then put into a list
        # the list becomes the argument to join()
        print(f"{name}'s favorite numbers are {' and '.join([str(num) for num in persons_fav_numbers])}")
# print(f"{name}'s favorite numbers are {' and '.join([str(num) for num in persons_fav_numbers if num %2 == 0])}")
# if num %2 == 0 --> an if statement inside a list comprehension
# meaning: if the remainder of num/2 == 0--> if the number is even


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
