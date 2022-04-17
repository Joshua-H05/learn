menu=("pizza", "pasta", "steak", "burgers", "tacos ")
for item in menu:
    print(item)
menu=("pizza", "pasta", "steak", "pork chops", "chicken wings") #can I convert the tuple to a list, change it and reconvert it to a tuple?
print("Here is our new menu:")
for item in menu:
    print(item.title())