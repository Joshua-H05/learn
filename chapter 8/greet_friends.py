def greet_friends(names):
    for name in names:
        print(f"Hello, {name}! How are you doing?")


friends_string = input("What are your friends' names? ")
friends = friends_string.split(",")
greet_friends(friends)


