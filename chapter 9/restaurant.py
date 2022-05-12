class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant. ")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open! ")


restaurant_1 = Restaurant("Butchers", "Burger")
restaurant_2 = Restaurant("Dominos", "Pizza")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
