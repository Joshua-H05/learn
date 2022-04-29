dream_vacation = {}
while True:
    name = input("What is your name? ")
    location = input("If you could visit one place in the world, where would you go? ")
    dream_vacation[name] = location
    repeat = input("Would you like another person to be asked? (yes/no) ")
    if repeat == "no":
        for name, response in dream_vacation.items():
            print(f"{name} would like to go to {response}")
        break
