def read_file(filename):
    try:
        with open(filename) as f:
            names = f.read().split()
    except FileNotFoundError:
        pass
        """print(f'Sorry, the file "{filename}" does not exist.')"""
    else:
        print(f"\nThese are the names that are currently stored in the file {filename}: ")
        for name in names:
            print(name)


files = ["dogs.txt", "cats.txt"]
for file in files:
    read_file(file)
