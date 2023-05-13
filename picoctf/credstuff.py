def find_user(username):
    with open("usernames.txt", "r") as u:
        with open("passwords.txt", "r") as p:
            for user, password in zip(u, p):
                if user.strip() == username:
                    print(f"User: {user.strip()}\nPassword: {password.strip()}")


find_user("cultiris")
