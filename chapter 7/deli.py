sandwich_orders = ["ham", "cheese", "tuna", "peanut-butter and jelly", "pastrami"]
no_longer_available = "pastrami"
completed_orders = []
print(f"The deli has run out of {no_longer_available}")
while no_longer_available in sandwich_orders:
    sandwich_orders.remove(no_longer_available)
while sandwich_orders:
    completed_order = sandwich_orders.pop(0)
    print(f"I've made a {completed_order} sandwich. ")
    completed_orders.append(completed_order)
if len(sandwich_orders) == 0:
    print("All the sandwiches have been made. ")
