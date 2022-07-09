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


if __name__ == "__main__":
    get_new_username_and_fav_number()
