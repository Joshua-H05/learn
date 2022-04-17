"""#inspired by the note about sorting lists with capital letters on page 45
fruits=["Bananas", "apples", "Pears", "strawberries", "Oranges"]#original
fruits_string= f"{fruits}"#convert the list into a string
fruits_lower=fruits_string.lower()#apply the .lower() function to the string
fruits=[]#make fruits an empty list so I can add fruits_lower back into the list
fruits.append(fruits_lower) #add fruits_lower into the list--> the list should now have lower case values only
fruits=fruits[0] #seems that I've created a list inside the empty list. Why is this? To solve this, I redefined fruits using the index 0
print(fruits)#now I can no longer apply the sort function. Is it no longer a list?
"""


# Attempt nr.2
fruits=["Bananas", "apples", "Pears", "strawberries", "Oranges"]  # original
fruits_string= " ".join(fruits).lower()  # join(): for every fruit in fruits, join it with the string in front of the
# dot and then join everything together.
# applying 2 functions in a line--> method chaining--> saves extra line of code--> more efficient for python to do
# all of this in one step
print(fruits_string)
fruits_lower=list(fruits_string.lower())
fruits_lower.sort()
print(fruits_lower)


"""new_fruits= []
for fruit in fruits:
    new_fruits.append(fruit.lower())
new_fruits.sort()
print(new_fruits)"""
