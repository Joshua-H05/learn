questions = ("What", "who", "Why", "how", "which")   # tuple,not changeable
answers = []   # list (empty)
for question in questions:
    answer = input(f"{question}: ")
    answers.append(answer)   # appending the "answer" string variable into the list

for index in range(len(answers)):   # "index": variable for type integer;
    print(questions[index], answers[index])
    # a for loop is a finite iteration; value from "range(len(answers))" is taken and assigned to the variable "index"
    # once the loop is complete, the next integer is assigned, process repeats until all integers have been used 
