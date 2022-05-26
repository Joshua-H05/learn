class User:
    def __init__(self, first_name, last_name, age, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f"{first_name} {last_name}"
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

    def profile_maker(self):
        vowels = ["a", "e", "i", "o", "u"]
        if self.occupation[0] in vowels:  # why is self.occupation not a string? (cannot apply lower function)
            # in fact, I cannot apply string functions to any of these self variables...
            print(f"{self.name} is {self.age} years old and is an {self.occupation} ")
        else:
            print(f"{self.name} is {self.age} years old and is a {self.occupation} ")

    def greet_user(self):
        print(f"Hello, {self.name}")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"The user {self.first_name} {self.last_name} has tried to log in")

    def total_login_attempts(self):
        print(f"The user {self.first_name} {self.last_name} has tried to log in a total of {self.login_attempts} times")

    def login_reset(self):
        self.login_attempts = 0


person_1 = User("Joshua", "Hu", 16, "student")
person_1.profile_maker()
person_1.greet_user()
for value in range(5):
    person_1.increment_login_attempts()
person_1.total_login_attempts()
person_1.login_reset()
person_1.total_login_attempts()



