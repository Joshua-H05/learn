class Student:  # move this to the bottom and make an instance of the class faculty an attribute of this class
    def __init__(self, first_name, last_name, age, gender, faculty, year_of_graduation, middle_name="", ):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.age = age
        self.gender = gender
        self.faculty = faculty
        self.year_of_graduation = year_of_graduation
        self.gpa = 0

    # The code used for initializing seems quite repetitive. Is there a function that can do it for you?
    #  If not, would there be a point in making one?

    def print_student_info(self):
        """A student is a member of a member of an educational institution who is paying for education"""
        if self.middle_name:
            print(f"{self.first_name} {self.middle_name} {self.last_name} is a {self.age} year old {self.gender}"
                  f"This student is a member of the faculty of {self.faculty} "
                  f"and will graduate in {self.year_of_graduation}. ")
        else:
            print(f"{self.first_name} {self.last_name} is a {self.age} year old {self.gender}. "
                  f"This student is a member of the faculty of {self.faculty} "
                  f"and will graduate in {self.year_of_graduation}. ")

    def show_student_gpa(self, gpa):
        self.gpa = gpa
        if self.middle_name:
            print(f"{self.first_name} {self.middle_name} {self.last_name} currently has a GPA of {self.gpa}")
        else:
            print(f"{self.first_name} {self.last_name} currently has a GPA of {self.gpa}")


class Professor:
    """A professor is an academic who is paid to provide intuition at an educational institute"""
# Move this down and make an instance of the class subjects an attribute of the class
    def __init__(self, first_name, last_name, *lectured_subjects, middle_name=""):
        self.first_name = first_name
        self.last_name = last_name
        self.lectured_subjects = lectured_subjects
        self.middle_name = middle_name

    def introduce_professor(self):
        if self.middle_name:
            print(f"{self.first_name} {self.middle_name} {self.last_name} lectures the following subjects:")
        else:
            print(f"{self.first_name} {self.last_name} lectures the following subjects:")
        for subject in self.lectured_subjects:
            print(subject)


class Subject:
    """ A subject is a branch of knowledge studied or taught in a school, college, or university"""

    def __init__(self, subject):
        self.subject = subject

    def subject_info(self):
        print(f"The subject {self.subject} is offered by this university")


class Course:
    def __init__(self, name, number_of_students):
        """A course is a set of classes on a specific subject taught by a professor"""
        # Can I create instances of two classes that are attributes of each other?
        self.name = name
        self.number_of_students = number_of_students

        """self.professor = Professor()
        self.subject = Subject()"""

    def course_info(self):
        print(f"{self.name} is a {self.subject.subject}course taught by professor {self.professor.last_name} "
              f"with {self.number_of_students} students.")


class Faculty:
    """A faculty is a department of an educational institute offering a set of courses concerned with a division of
    knowledge"""

    def __init__(self, name):
        self.name = name
        """self.courses = Course()"""

    def faculty_info(self):
        # Would I be able to add an arg to this and make it take an arbitrary number of courses?
        print(f"The faculty of {self.name} contains the course {self.course.name}, "
              f"which is taught by {self.course.professor}")


student_1 = Student("Joshua", "Hu", 16, "male", "computer science", 2024)
student_1.print_student_info()
student_1.show_student_gpa(5.6)
professor_1 = Professor("Albert", "Einstein", "Relativity", "mechanics")
professor_1.introduce_professor()
course_1 = Course("introduction to Python", 300)
course_1.course_info()

# Question: How can I make specific instances of classes attributes of a class?


