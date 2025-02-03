'''
Assignment

TechWorld, a technology training center, wants to allocate courses for instructors.
An instructor is identified by name, technology skills, experience and average feedback.
An instructor is allocated a course, if he/she satisfies the below two conditions:

eligibility criteria

- if experience is more than 3 years, average feedback should be 4.5 or more

- if experience is 3 years or less, average feedback should be 4 or more

he/she should posses the technology skill for the course

Identify the class name and attributes to represent instructors. Drag and drop the chosen class name, attributes and methods into the appropriate section of the box shown below
'''


class Instructor:
    def __init__(self, name, technology_skills, experience, average_feedback):
        self.__name = name
        self.__technology_skills = technology_skills  
        self.__experience = experience
        self.__average_feedback = average_feedback

    def get_name(self):
        return self.__name

    def get_technology_skills(self):
        return self.__technology_skills

    def get_experience(self):
        return self.__experience

    def get_average_feedback(self):
        return self.__average_feedback

    def is_eligible(self):
        if self.__experience > 3:
            return self.__average_feedback >= 4.5
        else:
            return self.__average_feedback >= 4

    def allocate_course(self, course_skill):
        if self.is_eligible() and course_skill in self.__technology_skills:
            return f"Course on '{course_skill}' allocated to {self.__name}."
        else:
            return f"{self.__name} is not eligible or does not have the skill '{course_skill}'."
