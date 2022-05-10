def make_car(manufacturer, model, **kwargs):  # What does "kwargs" stand for?
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs


print(make_car("Subaru", "outback", color="blue", price=20000))
# is the fact that the manufacturer & model key value pairs are at the end of the dictionary because the arbitrary
# keyword arguments are already in the dictionary and everything has to be added afterwards?
