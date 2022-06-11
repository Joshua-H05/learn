# pip install peewee

from datetime import date  # What is datetime and what is date?
import os  # what is os?
from peewee import *

os.remove("people.db")  # removes anything called "people" in the database to prevent potential confusion

db = SqliteDatabase('people.db')  # creates the database "people.db" and abbreviates it


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


# What does this do? Does it have anything to do with Meta classes?


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')  # This variable requires a foreign key so that this pet as an owner
    # to whom he is associated. This allows one person to have multiple pets but not vice versa
    # What exactly does backref do? Why does the foreign key "Person" not suffice?
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db  # this model uses the "people.db" database


def create_tables(database):
    database.create_tables([Person, Pet])


# Tells the database to create 2 tables, Person and Pet. The number of columns each table has is determined by the
# number of variables set when defining the respective classes


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
# There doesn't seem to be a person ID used to identify the person. Is it because this is an example?


def update_data(grandma):  # Why is grandma in parentheses?
    grandma.name = 'Grandma L.'
    grandma.save()  # Update grandma's name in the database.


def set_pet_owners():
    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(
        owner=herb, name='Mittens Jr', animal_type='cat')
    return bob_kitty, herb_fido, herb_mittens, herb_mittens_jr
# I noticed there isn't a function for creating pets without defining their owners. Is there any way I could create
# an instance of a pet, add it to the "Pet" table and then come back and assign an owner?
# Would this cause potential issues? (would the existence of instances without foreign keys mess up the program?)
# Why do the pets not have to be saved with the .save() function? Is it because they're associated to their owners
# with the foreign key "Person" and therefore is automatically saved when a person is saved?
# What happens if the owner assigned to a pet doesn't exist (e.g. due to a mistake)


def delete_pet(herb_mittens):  # Deletes the pet "Mittens" from the table of pets
    herb_mittens.delete_instance()


def show_someones_pets():
    # 1
    Person.get(Person.name == 'Grandma L.')  # selects the person with the name "Grandma L." in the "Person" table
    # using the get() function

    for person in Person.select():
        print(person.name)
# Why is the for loop necessary? Is it because it allows for multiple people to be printed?
# What is Person.select()?
    # 2
    query = (Pet
             .select(Pet, Person)
             .join(Person)
             .where(Pet.animal_type == 'cat'))  # Sets a condition of the instances being selected

    for pet in query:
        print(pet.name, pet.owner.name)  # Would this be used for printing specific columns in the database?

    # 3
    for pet in Pet.select().join(Person).where(Person.name == 'Bob'):  # Select the row in the pet table where the
        # person's name is Bob
        # Is the .join() function used because data needs to be pulled from both tables?
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
