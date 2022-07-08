filename = "addition_records.txt"


def addition(number_1, number_2):
    result = number_1 + number_2
    print(f"{num1} plus {num2} is {result}")


while True:
    num1 = input("Please type in the first number you would like to add or press q to quit: ")
    if num1 == "q":
        break
    else:
        num2 = input("Please type in the second number you would like to add: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            print("You can only add numbers! ")
        else:
            addition(num1, num2)
            answer = num1 + num2
            with open(filename, "a") as f:
                f.write(f"{num1} + {num2} = {answer}\n")
