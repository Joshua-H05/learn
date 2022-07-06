filename = "questions_chapter_10"
with open(filename) as file_object:
    questions = file_object.read()
    print(questions)

with open(filename) as file_object:
    for line in file_object:
        print(line.strip().replace("Perhaps", "maybe"))
        # Why does python print every single letter separately if I write "questions" instead of "file object"?
        # Hypothesis: "file_object" is a representation of the original text,
        # whereas the variable "questions" is a giant string containing all the information of the original file
        # so when a string is sliced, every letter is seen as an independent entity, which is why each letter occupies
        # a whole line

with open(filename) as file_object:
    lines = file_object.readlines()
questions_list = ""

for line in lines:
    questions_list += line
print(f"{questions_list}")
print(len(questions_list))
# Why do I have to open the file multiple times? Why does opening the file once as I've done below not suffice?

"""filename = "questions_chapter_10"
with open(filename) as file_object:
    questions = file_object.read()
    print(questions)

    for line in file_object:
        print(line.strip())
        # Why does python print every single letter separately if I write "questions" instead of "file object"?
        # Hypothesis: "file_object" is a representation of the original text,
        # whereas the variable "questions" is a giant string containing all the information of the original file
        # so when a string is sliced, every letter is seen as an independent entity, which is why each letter occupies
        # a whole line
    lines = file_object.readlines()
questions_list = ""
for line in lines:
    questions_list += line
print(f"{questions_list}")
print(len(questions_list))"""
