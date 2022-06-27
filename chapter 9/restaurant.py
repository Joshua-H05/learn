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
            print(f"{self.customers_served} customers have been served so far.")
        else:
            print("You cannot un-serve a customer -_-")

    def increment_customers_served(self, addition):
        if addition == 0:
            print("No need to update. The amount of served customers has not changed. ")
        elif addition > 0:
            self.customers_served += addition
            print(f"{addition} more customers have been served.")
        elif addition < 0:
            print("You cannot un-serve a customer -_-")

    def show_number_served(self):
        print(f"{self.customers_served} customers have been served so far.")


class VeganRestaurant(Restaurant):  # Naming issue?
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, *flavors):
        super().__init__(restaurant_name, cuisine_type)  # The *arg flavors should not go under super as super is
        # only used to allow one to call functions from the parent class
        self.flavors = flavors

    def show_flavors(self):
        print("Here are the available flavors:")
        for flavor in self.flavors:
            print(f"{flavor}")


if __name__ == "__main__":
    restaurant_1 = Restaurant("Butchers", "Burger")
    restaurant_2 = Restaurant("Dominos", "Pizza")
    restaurant_1.describe_restaurant()
    restaurant_1.open_restaurant()
    restaurant_1.show_number_served()
    restaurant_1.set_customers_served(5)
    restaurant_1.increment_customers_served(0)
    restaurant_1.increment_customers_served(10)
    restaurant_1.show_number_served()
    restaurant_2.describe_restaurant()
    restaurant_2.open_restaurant()
    vegan_restaurant_1 = VeganRestaurant("puccini", "Italian")
    ice_cream_stand_1 = IceCreamStand("chocolate", "mint", "vanilla", "strawberry")
    ice_cream_stand_1.show_flavors()
