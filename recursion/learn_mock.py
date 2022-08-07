# Identity function (returns its parameter)
def mprint(string_to_print):
    return string_to_print


myvariable = "Hello, how are you doing?"
assert print(myvariable) is None
print = mprint  # temporarily overwrites the original print function and assigns it a new function
# The reason there are no parentheses is that we're accessing the variables that store the function and not trying to
# execute the code a function stores
# this works the exact same way as assigning any variable a new value--> the variable that stores the code that prints
# something is assigned code that simply returns something
assert print(myvariable) == "Hello, how are you doing?" # Due to line 8, print(myvariable) now just returns myvariable
