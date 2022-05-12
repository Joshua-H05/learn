class User:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}"
        self.age = age
        self.occupation = occupation
    def profile_maker(self):
        vowels = ["a", "e", "i", "o", "u"]
        if self.occupation[0] in vowels:  # why is self.occupation not a string? (cannot apply lower function)
            # in fact, I cannot apply string functions to any of these self variables...
            print(f"{self.name} is {self.age} years old and is an {self.occupation} ")
        else:
            print(f"{self.name} is {self.age} years old and is a {self.occupation} ")
    def greet_user(self):
        print(f"Hello, {self.name}")
person_1 = User("Joshua", "Hu", 16, "student")
person_1.profile_maker()
person_1.greet_user()