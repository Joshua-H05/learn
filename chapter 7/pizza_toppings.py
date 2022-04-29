order = []
while True:
    topping = input("What would you like on your pizza?")
    if topping == "done":
        print(f"This is your final order: {', '.join(order)}")
        break
    else:
        order.append(topping)
        print(f"{topping} has been added to your pizza")


order = []
active = True
while active:
    topping = input("What would you like on your pizza?")
    if topping == "done":
        print(f"This is your final order: {', '.join(order)}")
        active = False
    else:
        order.append(topping)
        print(f"{topping} has been added to your pizza")


order = []
topping = ""
while topping != "done":
    topping = input("What would you like on your pizza?")
    if topping == "done":
        print(f"This is your final order: {', '.join(order)}")
    else:
        order.append(topping)
        print(f"{topping} has been added to your pizza")