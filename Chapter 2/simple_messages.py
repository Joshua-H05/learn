message_1= "how are you doing ?"
answer_1= input("What's your name?") #prompts input

print(f"Hello, {answer_1.title(),message_1}")
#f string: Replaces name of variable in braces with value
#variables must be enclosed in curly braces separately, or else single quotes show up and enclose the separate strings:
# e.g. Hello, ('Joshua', 'how are you doing ?') Reason: if everything is in one brace, python converts the 2 variables
# into a tuple first and then the print fucntion prints the tuple--> each variable should be enclosed in curly braces separately



