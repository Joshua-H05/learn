current_users = ["michael", "tom", "james", "max", "jack"]
new_users = ["Sarah", "TOm", "Lisa", "Max", "Lily"]
if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print("Sorry, your username has been taken, please select another one.")
        else:
            print(f"Welcome, {new_user}")
