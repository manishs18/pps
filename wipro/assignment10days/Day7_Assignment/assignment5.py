'''
Problem Statement

Tech World, a technology training center, wants to allocate courses for instructors. 
An instructor is identified by name, technology skills, experience and average feedback. 
An Instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria:

- If experience is more than 3 years, average feedback should be 4.5 or more 
- if experience is 3 years or less, average feedback should be 4 or more
he/she should posses the technology skill for the course

Identify the class name and attributes from the list of options below to represent instructors.

check eligibility()
avg feedback
experience
Instructor_name
allocate_course()
allocate_course(technolody)
__init__()
Instructor
calculate_avg_feedback()
technology skill


Write a Python program to implement the class chosen with its attributes and methods.

Note:

1. Consider all instance variables to be private and methods to be public
2. An instructor may have multiple technology skills, so consider instance variable, technology skill to be a list 
3. check eligibility(): Return true if eligibility criteria is satisfied

by the instructor. Else, return false 4. allocate_course(technology): Return true if the course which requires the given technology can be allocated to the instructor. Else, return false 5. Perform case sensitive string comparison

Represent few objects of the class, initialize instance variables using setter methods, invoke appropriate methods and test your program.
'''


class Instructor:
    def __init__(self):
        
        self.__name = None
        self.__technology_skills = []
        self.__experience = 0
        self.__avg_feedback = 0.0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_technology_skills(self):
        return self.__technology_skills

    def set_technology_skills(self, skills):
        if not isinstance(skills, list):
            raise ValueError("Technology skills should be a list")
        self.__technology_skills = skills

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        if experience < 0:
            raise ValueError("Experience cannot be negative")
        self.__experience = experience

    def get_avg_feedback(self):
        return self.__avg_feedback

    def set_avg_feedback(self, avg_feedback):
        if avg_feedback < 0 or avg_feedback > 5:
            raise ValueError("Average feedback should be between 0 and 5")
        self.__avg_feedback = avg_feedback

    def check_eligibility(self):
        if self.__experience > 3 and self.__avg_feedback >= 4.5:
            return True
        elif self.__experience <= 3 and self.__avg_feedback >= 4:
            return True
        return False

    def allocate_course(self, technology):

        if technology in self.__technology_skills:
            return self.check_eligibility()
        return False


instructor1 = Instructor()
instructor2 = Instructor()


instructor1.set_name("Amit")
instructor1.set_technology_skills(["Python"])
instructor1.set_experience(4)
instructor1.set_avg_feedback(4.6)

instructor2.set_name("Amit2")
instructor2.set_technology_skills(["Node.js"])
instructor2.set_experience(2)
instructor2.set_avg_feedback(4.2)

print(f"Instructor: {instructor1.get_name()}")
print(f"Eligible: {instructor1.check_eligibility()}")
print(f"Can allocate Python course: {instructor1.allocate_course('Python')}")

print("\nInstructor: Amit")
print(f"Eligible: {instructor2.check_eligibility()}")
print(f"Can allocate React course: {instructor2.allocate_course('React')}")
print(f"Can allocate Python course: {instructor2.allocate_course('Python')}")


