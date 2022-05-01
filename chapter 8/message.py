information = {}
def message(name, learning):
    print(f"{name} is currently learning {learning}.\n ")
while True:
    name = input("What's your name? ")
    learning = input("What are you learning right now? ")
    information[name] = learning
    message(name, learning)
    rerun = input("Would you like another person to be asked? (yes/ no) ").lower()
    if rerun == "no":
        print("Here is a list of all the information I've obtained:")
        for name, learning in information.items():
            message(name, learning)
        break
