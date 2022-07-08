def word_counter(filename, string):
    try:
        with open(filename) as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Sorry, but {filename} was not found. ")
    else:
        number_of_words = text.lower().count(f"{string} ")
        print(f'The word "{string}" showed up approximately {number_of_words} times in the file "{filename}". ')


while True:
    file = input("Which file would you like to analyse? Press q to quit: ")
    if file == "q":
        break
    word = input(f"Which word would you like to search for in the file {file}?: ")
    word_counter(file, word)
