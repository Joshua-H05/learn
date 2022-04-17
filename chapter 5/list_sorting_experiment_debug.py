fruits = ["Bananas", "apples", "Pears", "strawberries", "Oranges"]#original
fruit_string = " ".join(fruits)  # join(): for every fruit in fruits, join it with the string in front of the dot and
# then join everything together.
my_string = "abc,def,ghi,x,y,z"
my_list = my_string.split(",")  # divides a string into list entries based on a specified character
my_list = tuple(my_list)
print(my_list)
"""print(my_list)
print(fruit_string)
fruits_string= f"{fruits}"#convert the list into a string
print(fruits_string)
fruits_lower=list(fruits_string.lower())#apply the .lower() function to the string and assign the strings to a list
#Every letter is a now a separate value of the list...
print(len(fruits_lower))#The len function, however, shows that I only have 5 items in the list
fruits_lower.sort()#the sort function separates the letters, why?
print(fruits_lower)"""
