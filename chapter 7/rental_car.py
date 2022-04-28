requested_car = input("What kind of rental car would you like? ")
available_cars = ["BMW", "Mercedes", "Jeep", "Range rover", "Tesla"]
if requested_car == "bmw":
    requested_car = requested_car.upper()
else:
    requested_car = requested_car.title()
if requested_car in available_cars:
    print(f"We'll try to get you a {requested_car.title()}.")
else:
    print(f"Sorry, we don't have a {requested_car} available right now.")
