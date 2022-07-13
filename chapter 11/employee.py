class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5_000):
        self.salary += amount


if __name__ == "__main__":
    joshua_hu = Employee("Joshua", "Hu", 40_000)
    joshua_hu.give_raise()
    joshua_hu.give_raise(10_000)
    print(joshua_hu.salary)
