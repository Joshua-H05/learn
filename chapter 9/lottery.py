import pysnooper
from random import choice


characters = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "a", "b", "c", "d", "e")


@pysnooper.snoop()  # must be put immediately before the functioning code (not list/ tuple definitions etc.)
def show_winning_sequence():
    winning_sequence = []
    [winning_sequence.append(choice(characters)) for value in range(4)]
    return winning_sequence


ws = show_winning_sequence()
print(ws)

sequence = []
iterations = 0
while sequence != ws:
    sequence.clear()
    [sequence.append(choice(characters)) for value in range(4)]
    iterations += 1


print(f"{iterations}")
