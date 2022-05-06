def sandwich_maker(*ingredients):
    """Takes a list of ingredients for a sandwich and summarizes the order"""
    print("Making a sandwich with these ingredients:")
    for ingredient in ingredients:
        print(f" -{ingredient}")


sandwich_maker("cucumbers", "ham", "cheese", "tomatoes")
