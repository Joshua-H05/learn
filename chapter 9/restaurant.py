import pysnooper


@pysnooper.snoop()
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant. ")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open! ")

    def set_customers_served(self, number):
        if number >= self.customers_served:
            self.customers_served = number
        else:
            print("You cannot un-serve a customer -_-")

    def increment_customers_served(self, addition):
        if addition > 0:
            self.customers_served += addition
            print("Number of served customer hasn't changed. No need to update data")
        elif addition < 0:
            print("You cannot un-serve a customer -_-")


restaurant_1 = Restaurant("Butchers", "Burger")
restaurant_2 = Restaurant("Dominos", "Pizza")
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print(f"{restaurant_1.customers_served}")
restaurant_1.set_customers_served(5)
restaurant_1.increment_customers_served(10)
print(restaurant_1.customers_served)
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
