import json

filename = "usernames_and_favorite_numbers.json"


def get_new_username_and_fav_number():
    user_info = {}
    while True:
        username = str(input("What's your name? Press q to quit ")).title()
        if username.lower() == "q":
            print("Thanks! Your information has been stored. ")
            break
        else:
            try:
                fav_number = int(input("What is your favorite number? "))
            except ValueError:
                print("You can only type in a number! ")
                fav_number = int(input("Please type in a number: "))
                user_info[username] = fav_number
            else:
                user_info[username] = fav_number
    with open(filename, "w") as f:
        json.dump(user_info, f)


def display_favorite_number(name):
    try:
        with open(filename) as f:
            user_info = dict(json.load(f))
    except FileNotFoundError:
        return None
    else:
        if name in user_info.keys():
            print(f"Hello, {name}, your favorite number is {user_info[name]} ")


def get_stored_usernames():
    try:
        with open(filename) as f:
            user_info = dict(json.load(f))
            names = []
    except FileNotFoundError:
        return None
    else:
        for name in user_info.keys():
            names.append(name)
        return names


def greet_user():
    names = get_stored_usernames()
    username = input("What is your name?").title()
    if username in names:
        display_favorite_number(username)
    else:
        get_new_username_and_fav_number()


if __name__ == "__main__":
    greet_user()