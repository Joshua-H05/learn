name = input("What's your name?")
friends_names = input("what are your friends' names?")
names = f"{name} {friends_names}"
print(f"\n\t{names.title().strip()}")
# first convert values of the variable "names" into a string, and then apply the functions to add whitespace
print(f"\n\t{name.title().strip()} {friends_names.title().strip()}")
# which one is better?
# why does the strip function not work? Does it have to do with the order in which the code is written?
