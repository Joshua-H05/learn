pizzas=["pepperoni pizza", "pizza hawaii", "margherita pizza"] #original list of pizzas
pizzas.sort(reverse=True) #sort in reverse alphabetical order
for pizza in pizzas:
    print(f"I ordered a {pizza.title()}.") #Prints a line saying "I ordered..." for each pizza
print("I love pizza!")
friend_pizzas=pizzas.copy()#use the copy function to assign the current value of pizzas to the list friend_pizzas (using friend_pizzas=pizzas[:] is also possible
new_order= "BBQ pizza"#defining a new variable with a new type of pizza
pizzas.insert(2,new_order)#inserting the variable into the pizzas list using the new_order variable& the insert() function
new_order_friend= "meat pizza"#defining a new variable for my friend's new order with a new type of pizza
friend_pizzas.insert(1,new_order_friend)#inserting the variable into the friend_pizzas list using the new_order variable& the insert() function
print(f"We've made a new order! I've ordered a {new_order.title()} and my friend has ordered a {new_order_friend.title()}!")#print a message stating the new pizzas we've ordered
cancelled_order= "margherita pizza"#defining a the variable cancelled_order with the pizza I no longer want
friend_pizzas.remove(cancelled_order)#removing the pizza I no longer want from the list using the cancelled_order variable& the remove() function
print(f"My friend no longer wants his{cancelled_order.title()} so he has cancelled that order")#Print a message stating that my friend no longer wants the pizza assigned to the cancelled_order variable
print(f"This is my final order: {', '.join(pizzas)}.\n")# print a message with my final order
print(f"This is my friend's final order: {', '.join(friend_pizzas)}.") #print a message with my friend's final order
