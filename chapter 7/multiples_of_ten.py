prompt = "Give me a number and I'll tell you if it's a multiple of 10: "
prompt += "\n press q and then enter to quit "
number = input(prompt)  # I can't put the input function here only because if I do, the same code will run forever
# e.g. I type in 3--> "3 is not a multiple of 10" will be printed forever
while number != "q":
    # I can't put the input function here because
    # if the input function goes after the while loop, "number" will be undefined
    number = int(number)
    if number % 10 == 0:
        print(f"{number} is a multiple of 10")
    else:
        print(f"{number} is not a multiple of 10")
    number = input(prompt)
# Question: Is there a way to achieve the same effect by using the input function only once?

# Solution:
prompt = "Give me a number and I'll tell you if it's a multiple of 10: "
prompt += "\n press q and then enter to quit "
number = ""
while number != "q":
    number = input(prompt)
    if number != "q":
        number = int(number)
        if number % 10 == 0:
            print(f"{number} is a multiple of 10")
        else:
            print(f"{number} is not a multiple of 10")
# Which is better?

prompt = "Give me a number and I'll tell you if it's a multiple of 10: "
prompt += "\n press q and then enter to quit "
active = True
while active:
    number = input(prompt)
    if number == "q":
        active = False
    else:
        number = int(number)
        if number % 10 == 0:
            print(f"{number} is a multiple of 10")
        else:
            print(f"{number} is not a multiple of 10")


prompt = "Give me a number and I'll tell you if it's a multiple of 10: "
prompt += "\n press q and then enter to quit "
number = ""
while True:
    number = input(prompt)
    if number == "q":
        break
    number = int(number)
    if number % 10 == 0:
        print(f"{number} is a multiple of 10")
    else:
        print(f"{number} is not a multiple of 10")
