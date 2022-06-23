import os
from datetime import date

from peewee import *

db = SqliteDatabase("educational_institute.db")


# Creates file on disk called "educational institute" if it doesn't exist uses if exists


class University(Model):
    school_ID = AutoField()  # creates unique sequence of integers, guarantees each school has a unique ID,
    # Should be put first (convention)
    name = CharField()
    founding_date = DateField()

    class Meta:
        database = db


class Faculty(Model):
    university = ForeignKeyField(University, backref="university")
    name = CharField()
    number_of_students = IntegerField()

    class Meta:
        database = db


class Student(Model):
    university = ForeignKeyField(University, backref="student")
    faculty = ForeignKeyField(Faculty, backref="student")
    student_ID = AutoField()
    name = CharField()
    age = IntegerField()  # By using age as a variable, data is concealed--> use birthday because age is derived from it

    # autofield: automatically generates an identifier for each database table-> unique primary key ensured

    class Meta:
        database = db


class Professor(Model):
    professor_ID = AutoField()
    university = ForeignKeyField(University, backref="professor")
    # multiple faculties?

    name = CharField()

    class Meta:
        database = db


class ProfessorFaculty(Model):
    # Find lurking entities--> Class that needs to exist in order to combine the two-->use instead of foreign keys
    # Enables a multiple to multiple relationship
    # Many to many resolution tables: convention--> name after the two classes
    university = ForeignKeyField(University, backref="University")
    faculty = ForeignKeyField(Faculty, backref="faculty")

    class Meta:
        database = db


def create_tables(database):
    database.create_tables([University, Faculty, Student, Professor])


def add_data():
    harvard_university = University(name="Harvard", school_ID=1, founding_date=date(1636, 8, 9))
    oxford_university = University(name="Oxford", school_ID=2, founding_date="1096")
    # cannot use date due to lack fof info--> store in string format/ store the year only
    faculty_philosophy_harvard = Faculty(university=harvard_university, name="Philosophy",
                                         number_of_students=22947)
    faculty_cs_oxford = Faculty(university=oxford_university, name="Computer Science", number_of_students=25820)
    joshua_hu = Student(university=oxford_university, faculty=faculty_cs_oxford, student_ID=983, name="Joshua Hu",
                        age=21)
    professor_blunsom = Professor(university=oxford_university, name="Phil Blunsom",professor_ID=54)
    """blunsom_cs = ProfessorFaculty(professor= )"""

    harvard_university.save()
    oxford_university.save()
    faculty_philosophy_harvard.save()
    faculty_cs_oxford.save()
    joshua_hu.save()
    professor_blunsom.save()


def delete_university(harvard_university):
    harvard_university.delete_instance()


def show_faculty_students():
    """Faculty.select(Faculty.name == "Computer Science")
    for faculty in Faculty.select():
        print(f"{Faculty.name}")"""

    query = (Student
             .select(Student, Faculty, University)
             .join(Faculty, University)
             .where(University.name == "Oxford" & Faculty.name == "Computer Science"))
    results = db.execute(query)
    # The query is an sql statement--> sends sql to the database& runs--> returns data in
    # tabular format--> assign to variable to iterate around
    """for student in results:
        print(Student.name, Faculty.name, University.name)"""
    print(results)


if __name__ == "__main__":
    db.connect()
    create_tables(db)
    add_data()
    """delete_university(harvard_university)"""  # What's wrong here?
    show_faculty_students()
    db.close()

# can I use Datefield() if I only know the year?
# I noticed that Pycharm does not provide support when you're typing in the parameters. Why is this?
# Why do I have to type in the name of the variable as well?
# GENERAL RULE: write small amounts of code and test constantly
