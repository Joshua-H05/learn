import users
import admin

user_1 = users.User("Jack", "Ma", 57, "Entrepreneur")
user_1.greet_user()
admin_1 = admin.Admin("Joshua", "Hu", 16, "Student")
admin_1.greet_user()
admin_1.privileges.show_privileges()
admin_1.increment_login_attempts()
admin_1.total_login_attempts()
admin_1.login_reset()
admin_1.total_login_attempts()
joshua_privileges = users.Privileges(("delete posts", "block users", "unblock users"))
# This instance takes a tuple, so don't forget to put all the strings (privileges) into a tuple
joshua_privileges.show_privileges()
admin_1.privileges = joshua_privileges  # override the original instance of Privileges that was instantiated by default
# and assigned as an attribute
admin_1.privileges.show_privileges()
