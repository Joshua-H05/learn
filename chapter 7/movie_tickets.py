while True:
    age = input("What's your age? \n Press q to finish")
    if age == "q":
        break
    else:
        age = int(age)
    if age < 3:
        print("The ticket is free!")
    elif age < 12:
        print("Your ticket costs 10")
    elif age >= 12:
        print("Your ticket costs 15")