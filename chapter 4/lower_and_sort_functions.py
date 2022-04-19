fruits = ["Bananas", "apples", "Pears", "strawberries", "Oranges"]


# for lists only
def lower_lists(objects):  # defining the list
    for index in range(len(objects)):  # using the range() function in the for loop to get integers starting from zero
        # that are later used for slicing the list ( the range is obtained using the len() function, which tells you
        # the length of the list
        objects[index] = objects[index].lower()


lower_lists(fruits)
print(fruits)

"""print(lower(fruits))"""  # why does this return the value none? Is it because the function only sorts a list
# and doesn't return a value?

# for lists, tuples etc.
fruits = ("Bananas", "apples", "Pears", "strawberries", "Oranges")


def lower_all(objects):  # defining the list
    item_list = []  # this line cannot be put inside the for loop because if it is, the list is redefined as an
    # empty list at the beginning of each iteration
    for object in objects:
        item_list.append(object)  # this for loop turns the tuple into a list
    lower_lists(item_list)  # this line uses the previously defined function "lower_lists" to turn
    # the newly defined list into a list with lower case items only

# The return value must be used here because the function is meant to sort the function only and doesn't return a value
# This does not need to be done in the previous function because it simply processes a given list, whereas this one
# creates a list based on the given information and then processes it. If the return function isn't applied, python
# doesn't know what to do with the data. 
    return item_list


print(lower_all(fruits))

# Which version is better?
fruits = ("Bananas", "apples", "Pears", "strawberries", "Oranges")


def lower_all(objects):  # defining the list
    item_list = []  # this line cannot be put inside the for loop because if it is, the list is redefined as an
    # empty list at the beginning of each iteration
    for object in objects:  # what does "shadows built-in name 'object'" mean? (problems)
        item_list.append(object.lower())  # this for loop takes each item of the tuple, turns it into lower case
        # and appends it into the list "item_list"
    return item_list


print(lower_all(fruits))
