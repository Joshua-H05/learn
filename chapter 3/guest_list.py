guests = ["albert Einstein", "Michael Jordan", "Kobe Bryant", "Stephen Hawking"]
print(f"\t{guests}")  # Cannot use functions like strip() because they only work with strings
cannot_attend = "albert Einstein"
guests.remove(cannot_attend)
print(f"\tSadly, {cannot_attend.title()} will not be able to make it to the party.")
new_guest = "George Washington"
print(f"{new_guest} has been invited to the party")
guests.append(new_guest)
print(f"Here's the new list of invitees:{', '.join(guests)}.")
# I'm using an f string, why are there still single quotes?: printing a string representation of the list
# --> displays the string as if it were a list
# solution: added another string( comma& space)--> has all the functions that strings have-->
# . join removes the items from the list and joins them and separates them by the string at the beginning
# (in this case the command& space)
for guest in guests:
    print(f"Hey,{guest.title()} you have been invited to my party!")
print("I've found a larger table!")
new_guest2 = guests.insert(0, "Lebron James")
# Why "none": insert goes into a list and changes it in a place--> functions that belong to lists, job: modify the list
# these are functions with no specified return values, so they return "nothing"
new_guest3 = guests.insert(2, "Warren Buffett")
new_guest4 = guests.append("Elon Musk")
print(f"Here's a list of the new guests: {new_guest2} {new_guest3} {new_guest4}")
print(f"Here's the new list of invitees:{guests}")

# v2 I wrote this because lines 13, 14&15 don't function

guests = ["albert Einstein", "Michael Jordan", "Kobe Bryant", "Stephen Hawking"]  # initial list of guests
print(
    f"\t{guests}")  # why can't I add functions like .strip()?--> Can only be applied to strings--> must be converted to
# string before using
cannot_attend = "albert Einstein"  # Define Einstein as a guest who cannot attend
guests.remove(cannot_attend)  # use the remove function to remove Einstein
print(
    f"\tSadly, {cannot_attend.title()} will not be able to make it to the party.")
# Message stating that the string assigned to cannot_attend (n this case , Einstein) will not be able to attend
new_guest = "George Washington"  # define a new guest
print(
    f"{new_guest} has been invited to the party")
# message stating that the string assigned to new_guest has been invited to the party
guests.append(new_guest)  # use the append function to add new_guest to the end of the list
print(
    f"Here's the new list of invitees:{', '.join(guests)}.")
# I'm using an f string, why are there still single quotes?: printing a string representation of the list-->
# displays the string as if it were a list
# solution: added another string( comma& space)--> has all the functions that strings have-->
# . join removes the items from the list and joins them and separates them by the string at the beginning
# (in this case the comma& space)
for guest in guests:
    print(
        f"Hey,{guest.title()} you have been invited to my party!")
    # using a for loop to print the same message for each of the guests
print("I've found a larger table!")
new_guest2 = "Lebron James"
new_guest3 = "Warren Buffett"
new_guest4 = "Elon Musk"
guests.insert(0, new_guest2)  # can I combine the two "inserts" and make them one line?
guests.insert(2, new_guest3)  # insert the guests in designated places in the list
guests.append(new_guest4)  # use the append function to add to the end of the list
print(f"Here's a list of the new guests: {new_guest2} {new_guest3} {new_guest4}")  # prints the new guests
print(f"Here's the new list of invitees:{guests}")  # prints the updated guest list
print("sadly, I will only be able to invite two people tonight.")
print(guests)  # confirmation: prints the newest version of the list
no_longer_invited1 = guests.pop(0)
no_longer_invited2 = guests.pop(1)
no_longer_invited3 = guests.pop(1)
no_longer_invited4 = guests.pop(1)
# why out of range?Every time the pop function is used, the index numbers are changed, and you work with a modified list
no_longer_invited5 = guests.pop(1)
no_longer_invited = no_longer_invited1, no_longer_invited2, no_longer_invited3
for no_longer_invited_guest in no_longer_invited:
    print(f"I'm sorry, {no_longer_invited_guest}, you're no longer invited.")
print(f"{guests}")
del guests[:]  # if nothing is specified to the left of the colon, it means start from the beginning
# if nothing is specified to the right, it goes to the end. OR: use the clear function--> guests.clear()
print(f"guests{guests}")
