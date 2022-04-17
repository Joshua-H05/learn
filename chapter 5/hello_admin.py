users = ["admin", "Tom", "James", "Max", "Jack"]
if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to se a status report?")
        else:
            print(f"Hello, {user}.")
else:
    print("We need to get some users!")
