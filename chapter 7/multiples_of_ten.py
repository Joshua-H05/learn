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
number = ""  # Sets number as an empty string so that the program can be run the fist time around
while number != "q":
    number = input(prompt)  #
    if number != "q":  # If number is "q", this round of the program stops and python goes back to
        # the line "while number != "q":" and now that number = "q" the conditional testing fails and the code stops
        number = int(number)
        if number % 10 == 0:
            print(f"{number} is a multiple of 10")
        else:
            print(f"{number} is not a multiple of 10")
# Which is better?

prompt = "Give me a number and I'll tell you if it's a multiple of 10: "
prompt += "\n press q and then enter to quit "
active = True  # Flag: sets the variable "active" to equal True
while active:
    number = input(prompt)
    if number == "q":
        active = False  # If number =="q", the value of "active" is changed to equal False and the program stops running
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
    if number == "q":  # if the input is "q", stop the program
        break
    number = int(number)
    if number % 10 == 0:
        print(f"{number} is a multiple of 10")
    else:
        print(f"{number} is not a multiple of 10")


prompt = "Give me a number and I'll tell you if it's a multiple of 10: "
prompt += "\n press q and then enter to quit "
number = ""
while number != "q":
    number = input(prompt)  # asks for either a number or "q"
    if number == "q":
        continue  # if the input is q, go back to the beginning of the program and test the condition "number != "q" "
    number = int(number)  # if not, the program continues
    if number % 10 == 0:
            print(f"{number} is a multiple of 10")
    else:
            print(f"{number} is not a multiple of 10")

