def make_shirt(size="L", message="I love Python"):
    """Prints the requested size of the T-shirt and the message that should be printed on it"""
    print(f'You would like a t-shirt in size {size} with the message "{message}" printed on it.')


make_shirt()
make_shirt(size="M")
make_shirt(message="Hello", size="S")
make_shirt("S", "Hello")
