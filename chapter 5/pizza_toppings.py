# Inspired by "Testing multiple conditions" on page 83
toppings = list(input("What would you like on your pizza? "))  # Is there any way to make python put words into the list
# instead of individual letters?
print(toppings)

# Alternative
available = ["cheese", "pepperoni", "mushrooms", "sausage", "chicken"]
toppings_alt = []
first_topping = input("What would you like on your pizza? Please write one item only: ")
if first_topping in available:
    toppings_alt.append(first_topping)
else:
    replacement = input("Sorry, that is not available. Please select something else. ")
    toppings_alt.append(replacement)
answer = input("Would you like any other toppings? ")
if answer.lower() == "yes":
    number_of_extra_toppings = int(input("How many more would you like? Please type in a number only. "))
    for index in range(0, number_of_extra_toppings):
        extra_topping = input("Please type in one additional topping you would like: ")
        if extra_topping == first_topping.lower() or extra_topping in toppings_alt:
            alternative = input("You've already selected this topping. Please choose something different: ")
            toppings_alt.append(alternative)
        elif extra_topping in available:
            toppings_alt.append(extra_topping)
        else:
            replacement = input("Sorry, that is not available. Please select something else. ")
            toppings_alt.append(replacement)
elif answer.lower() == "no":
    print("Ok, coming right up!")


print(f"This is a list of toppings you've requested: {toppings_alt}\n")
