'''
Problem Statement

A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam. Data are valid, if:

- Age is greater than 20
- Marks is between 0 and 100 (both inclusive)

A student qualifies for admission, it

 - Age and marks are valid and 
 - Marks is 65 or more

Write a python program to represent the students seeking admission in the university.

The details of student class are given below.

Class name: Student

Attributes (private)    student id marks age
Methods (public)        __init__()                Create and initialize all instance variables to None
                        validate_marks()
                        validate_age()            If data is valid, return true. Else, return false 

                        check_qualification()     Validate marks and age.
                                                    If valid, check if marks is 65 or more.
                                                        If so return true 
                                                        Else return false
                                                    Else return false

                        setter methods            Include setter methods for all instance variables to set its values
                        getter methods            Include getter methods for all instance variables to get its values
'''

class Student:
    def __init__(self):
        self.__student_id = None
        self.__age = None
        self.__marks = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_age(self, age):
        self.__age = age

    def set_marks(self, marks):
        self.__marks = marks

    def get_student_id(self):
        return self.__student_id

    def get_age(self):
        return self.__age

    def get_marks(self):
        return self.__marks

    def validate_marks(self):
        return 0 <= self.__marks <= 100

    def validate_age(self):
        return self.__age > 20

    def check_qualification(self):
        if self.validate_age() and self.validate_marks():
            return self.__marks >= 65
        return False

student1 = Student()
student1.set_student_id("S001")
student1.set_age(21)
student1.set_marks(70)

print(f"Student ID: {student1.get_student_id()}")
print(f"Age Valid: {student1.validate_age()}")
print(f"Marks Valid: {student1.validate_marks()}")
print(f"Qualified for Admission: {student1.check_qualification()}")

student2 = Student()
student2.set_student_id("S002")
student2.set_age(19) 
student2.set_marks(85)

print(f"\nStudent ID: {student2.get_student_id()}")
print(f"Age Valid: {student2.validate_age()}")
print(f"Marks Valid: {student2.validate_marks()}")
print(f"Qualified for Admission: {student2.check_qualification()}")

