import json

filename = "users.json"


def register_new_user():
    username = input("What is your name?: ")
    with open(filename, "w") as f:
        json.dump(username, f)
    print(f"Thanks, {username}, we'll remember you next time! ")


def get_user():
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    user = get_user()
    if user:
        confirmation = input(f"Hello, are you {user}? Please answer y for yes and n for no: ")
        if confirmation == "y":
            print(f"Welcome back, {user}! ")
        elif confirmation == "n":
            register = input("Would you like to become a user? If so, please press y, if not, please press n: ")
            if register == "y":
                register_new_user()
            else:
                print("Thanks and hope see you soon!")
    else:
        register_new_user()


if __name__ == "__main__":
    greet_user()
