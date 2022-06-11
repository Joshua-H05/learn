# pip install peewee
# General structure: As I understand, the classes Pet and Person are created and the amount or parameters taken are
# defined. Next, functions are created to populate the table
from datetime import date  # What is datetime and what is date?
import os  # what is os?
from peewee import *

os.remove("people.db")  # Because this program is illustrating how a database functions--> remove the old database file
# to make sure the code works (e.g if you try to add something that is already there, the program will fail)--> delete
# everything to prevent ( the same should be done in tests but not in actual situations)

db = SqliteDatabase('people.db')  # creates the database "people.db" and abbreviates it
# Convention when using databases: db stores the result of instantiating hte sqlite database class--> When the database
# runs, it looks for a file called "people.db"--> Uses if found, creates if not


class Person(Model):
    name = CharField()
    # Specifies that this variable is a string--> behind the scenes the Model class converts it to the format required
    # by the database: Communicates with the database and obtains information on the format needed
    birthday = DateField()

    # Specifies that this variable is a date--> behind the scenes the Model class converts it to the format required
    # by the database
    # This is used because different databases have different requirements for the format of variables
    # Using this gives your code versatility, allowing it to function regardless of the type of database

    class Meta:
        database = db  # This model uses the "people.db" database.


# Complex function, must be there/ constant code
# Metaclass: Interferes behind the scenes with the instantiation of classes


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')  # This variable requires a foreign key so that this pet as an owner
    # to whom he is associated. This allows one person to have multiple pets but not vice versa
    # What exactly does backref do? Why does the foreign key "Person" not suffice?
    # Backref stores the name of the relationship in the database: In the database, there are tables you create (what
    # programmers usually see about the database) Table formats, column formats, keys etc. are defined in Sql in the
    # system databases  --> backref helps by better documenting the data in the database& makes things more efficient
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


def create_tables(database):
    database.create_tables([Person, Pet])


# Tells the database to create 2 tables, Person and Pet. Takes the parameters, which are classes defined above and
# generates the sql code used to create the database
# the number of columns each table has is determined by the
# number of variables set when defining the respective classes.
# Normally, create_tables() and the domain model are stored separately in different files (definition.py/ model.py)
# and definition.py would import model and the file with the actual data would as well. Definition.py must be stored
# separately because if it is run accidentally, it can delete the entire database


def add_data():
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    uncle_bob.save()  # bob is now stored in the database
    # Is this an inbuilt peewee function?
    # alt
    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
    grandma.save()
    herb.save()
    return uncle_bob, grandma, herb


# Does this mean that every time I need to add data to the database, I have to change this function?
# This is just an example, in reality this would not be the case. You would either put everything in a loop and use
# the loop to update the database or prompt of input and update the database accordingly
# For loops vs while loops:
    # For loops should be used when you know how many times you want to iterate
    # While loops when you don't know how many times/ want to iterate forever
    # In this case: While loop when you're asking the suer for input BUT the connection would need to be open the whole
    # time--> costly, but data is updated quickly--> safe if the database crashes

# There doesn't seem to be a person ID used to identify the person. Is it because this is an example?
# Relational database used to store data--> Primary keys are used to uniquely identify each record--> if an ID number
# is used, you could have duplicate entries (same person, same date but different keys)--> not always a good solution
# If an ID is not used, people who happen to have the same names, for example, would not be able to be stored in the
# same database


def update_data(grandma):  # Why is grandma in parentheses?: Because it's an instance--> all that needs to be done is
    # updating the name colum of this particular row
    grandma.name = 'Grandma L.'
    grandma.save()  # Update grandma's name in the database.


def set_pet_owners():
    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(
        owner=herb, name='Mittens Jr', animal_type='cat')
    bob_kitty.save()
    herb_fido.save()
    herb_mittens.save()
    herb_mittens_jr.save()
    return bob_kitty, herb_fido, herb_mittens, herb_mittens_jr
# I noticed there isn't a function for creating pets without defining their owners. Is there any way I could create
# an instance of a pet, add it to the "Pet" table and then come back and assign an owner?
    # Database protects integrity of data--> foreign key constraints--> set these up in database in domain model file
    # If you delete a person, all the pets associated with the person are deleted as well--> All the data is correct
# Would this cause potential issues? (would the existence of instances without foreign keys mess up the program?)
    # Yes, you would end up with data in database that cannot be used
# What happens if the owner assigned to a pet doesn't exist (e.g. due to a mistake)
    # Would not be possible


def delete_pet(herb_mittens):  # Deletes the pet "Mittens" from the table of pets
    herb_mittens.delete_instance()


def show_someones_pets():
    # 1
    Person.get(Person.name == 'Grandma L.')  # selects the person with the name "Grandma L." in the "Person" table
    # using the get() function

    for person in Person.select():
        print(person.name)
# Why is the for loop necessary? Is it because it allows for multiple people to be printed?--> Yes, the select method
# returns a list that can be iterated around
# What is Person.select()?
    # 2
    query = (Pet
             .select(Pet, Person)
             .join(Person)
             .where(Pet.animal_type == 'cat'))  # Sets a condition of the instances being selected
# Query: Select records in a database by specifying all or a subset of the columns--> results in all or a subset of the
# rows, you can join tables together& do summaries& calculations
# Leave the calculations to the database because it is more powerful& therefore faster
    for pet in query:
        print(pet.name, pet.owner.name)  # Would this be used for printing specific columns in the database?

    # 3
    for pet in Pet.select().join(Person).where(Person.name == 'Bob'):  # Select the row in the pet table where the
        # person's name is Bob
        # Is the .join() function used because data needs to be pulled from both tables? (connects the two based on
        print(pet.name)


if __name__ == "__main__":  # Makes sure this code is only run when the file is run locally--> won't run if it's
    # imported as a module
    db.connect()  # connects to the database
    create_tables(db)  # creates the database here abbreviated as "db"
    uncle_bob, grandma, herb = add_data()  # Why is this necessary? haven't the three people & their data
    # already been defined in the function
    update_data(grandma)
    bob_kitty, herb_fido, herb_mittens, herb_mittens_jr = set_pet_owners()
    delete_pet(herb_mittens)
    show_someones_pets()
    db.close()  # Connections are expensive--> Should be closed ASAP
