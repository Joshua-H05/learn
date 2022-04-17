name = "Bob"
print("is your your name == 'Bob'? I predict true")
print(name.lower() == "bob")

friends_name = "Tom"
print("is your your friend's name== 'Bob'? I predict false")
print(friends_name.lower() == "bob")

order = input("What type of pizza would you like for dinner?")
if order.lower() == "pepperoni" or order.lower() == "pepperoni pizza":
    print("Coming right up!")
else:
    print("Sorry, that is not available")

toppings = input("What toppings would you like?")
if toppings.lower() != "extra cheese":
    print("Don't put extra cheese")

age = int(input("How old are you?"))
friends_age = int(input("How old is your friends"))
if age >= 18:
    print("You're an adult")
else:
    print("You're a minor")
if age <= 18 or friends_age <= 18:
    print("One of you is a minor")
if age >= 18 or friends_age >= 18:
    print("At least one of you is an adult")
if age >= 18 and friends_age >= 18:
    print("Both of you are adults")

order = input("What fruits would you like to buy today?")
fruits = ["bananas", "apples", "pears", "strawberries", "oranges"]

if order.lower() in fruits:
    print("Here you go!")
else:
    print("Sorry, we're sold out!")

banned_users = ["Tom", "Max", "James"]
username = input("What's your name?")
if username.title() not in banned_users:
    print(f"Welcome, {username.title()}")
else:
    print(" Sorry, access denied.")
