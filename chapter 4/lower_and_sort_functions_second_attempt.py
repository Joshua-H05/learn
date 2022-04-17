fruits = ("Bananas", "apples", "Pears", "strawberries", "Oranges")
def lower_all(objects):  # defining the list
    item_list = []  # this line cannot be put inside the for loop because if it is, the list is redefined as an
    # empty list at the beginning of each iteration
    for object in objects:
        item_list.append(object.lower())  # this for loop takes each item of the tuple, turns it into lower case
        # and appends it into the list "item_list"
    return item_list
print(lower_all(fruits))
