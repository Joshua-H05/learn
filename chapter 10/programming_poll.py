filename = "programming_poll.txt"
people_and_reasons = {}
while True:
    name = input("What is your name? Press q to quit. ")
    if name == "q":
        for key, value in people_and_reasons.items():
            print(f"{key.title()} likes programming because {value}")
        break
    else:
        reason = input("Why do you like programming? ")
        people_and_reasons[name] = reason
        with open(filename, "a") as file_object:
            file_object.write(f"{name} : {reason}\n")
