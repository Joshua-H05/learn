from users import User

class Privileges:
    def __init__(self, list_of_privileges=("delete posts", "block users")):
        self.list_of_privileges = list_of_privileges

    def show_privileges(self):
        print(f"Here is a list of this admin's privileges: ")
        for privilege in self.list_of_privileges:
            print(f"{privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, occupation):
        # Is there any way of using an *arg to make the number of privileges arbitrary?
        super().__init__(first_name, last_name, age, occupation)
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = Privileges()


if __name__ == "__main__":
    person_1 = User("Joshua", "Hu", 16, "student")
    person_1.profile_maker()
    person_1.greet_user()
    for value in range(5):
        person_1.increment_login_attempts()
    person_1.total_login_attempts()
    person_1.login_reset()
    person_1.total_login_attempts()
    admin_1 = Admin("Joshua", "Hu", 16, "student")
    admin_1.greet_user()
    admin_1.privileges.show_privileges()
