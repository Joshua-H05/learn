guest_first_name = input("What is your first name? ")
guest_middle_name = input("What is your middle name? Press enter to skip if you don't have one. ")
guest_last_name = input("What is your last name? ")
guest_age = int(input("How old are you? "))
guest_nationality = input("What is your nationality? ")

guest_info = {"first name": guest_first_name,
              "last name": guest_last_name,
              "age": guest_age,
              "nationality": guest_nationality,
              }
if guest_middle_name:
    guest_info["middle name"] = guest_middle_name

print("This is the data you have provided: ")

filename = "guest.txt"
with open(filename, "a") as text_object:
    for key, value in guest_info.items():
        text_object.write(f"{key} : {value}\n")
        print(f"{key} : {value}")
