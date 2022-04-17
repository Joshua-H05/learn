fruits = ["Bananas", "apples", "Pears", "strawberries", "Oranges"]  # original
print(type(fruits))  # Verify the type of variable
lower_fruits = []
for fruit in fruits:
    lower_fruits.append(fruit.lower())
print(sorted(lower_fruits))

"""fruits = ["Bananas", "apples", "Pears", "strawberries", "Oranges"]  # original
for index in range(len(fruits)):
    fruits[index][0]= fruits[index][0].lower() # everything else in this program works but this line doesn't: This line 
    tries to take a part (the first letter) of a string out and replace it. 
    This doesn't work because strings are immutable.
print(fruits)"""

fruits = ["Bananas", "apples", "Pears", "strawberries", "Oranges"]  # original
for index in range(len(fruits)):
    fruits[index] = fruits[index].lower()
print(fruits)

fruits_t = tuple(fruits)  # changing the type of the variable--> casting
print(type(fruits_t))  # proof that fruits_t is indeed a tuple
fruits_t_s = sorted(fruits_t)  # tuples (in this case fruits_t) do support the sorted function as it doesn't change the
# original variable, however, in order to execute the function, python converts the tuple into a list automatically
print(type(fruits_t_s))  # proof that it's list now


def add_up(first_number, second_number):
    result = first_number + second_number
    return result


print(add_up(2, 3))  # addup(2,3) is a call to the function--> the output replaces the function conceptually

# reasons to use functions:
#   Makes code more understandable
#   Shortens code
#   You can define and validate functions and reuse them, reducing the chance of making mistakes
#   as you're using pre-validated code
# Always define a function using a name that clearly describes what it does
# Do not use the word "and" when naming a function because that indicates that the function you're trying to define is
# doing 2 different things and should therefore be separated into 2 different functions

# hw: write a function that converts lists into lower case and then sorts it ( not only lists, also tuples etc.)
