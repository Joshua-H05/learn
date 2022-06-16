class Car:
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year
        self.model = model
        self.odometer = 0

    def describe_car(self):
        description = f"This car is a {self.brand} {self.model} from {self.year}. "
        print(description)

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it. ")

    def increment_odometer(self, miles):  # Is there any way to include user input here?
        # E.g. ask how far they've driven the car
        if miles < 0:
            print("You can't roll the odometer back!")
        elif miles == 0:
            print("The mileage has remained the same. There is no need to update it.")
        else:
            self.odometer = self.odometer + miles
            print(f"Your odometer now reads {self.odometer}. ")

    def update_odometer(self, mileage):
        if mileage < self.odometer:
            print("You can't roll the odometer back!")
        else:
            self.odometer = mileage


class Battery:
    def __init__(self, capacity=75):
        self.capacity = capacity

    def describe_battery(self):
        print(f"This car has a {self.capacity} Kwh battery. ")


class ElectricCar(Car):
    def __init__(self, brand: object, year: object, model: object) -> object:
        super().__init__(brand, year, model)
        self.range = None
        self.battery_capacity = Battery().capacity

    def calculate_range(self):
        if self.battery_capacity == 75:
            self.range = 100
        elif self.battery_capacity == 100:
            self.range = 150
        elif self.range > 100:
            self.range = "Greater than 100"
        print(f"Your car's range is {self.range} miles")

    def upgrade_battery(self):
        if self.battery_capacity <= 75:
            self.battery_capacity = 100


# Why can't I add "if __name__ = "main"" here?

tesla_model_x = ElectricCar("Tesla", 2020, "model x")
tesla_model_x.calculate_range()
tesla_model_x.update_odometer(50)
tesla_model_x.increment_odometer(20)
tesla_model_x.read_odometer()
[tesla_model_x.upgrade_battery() for value in range(5)]
tesla_model_x.calculate_range()