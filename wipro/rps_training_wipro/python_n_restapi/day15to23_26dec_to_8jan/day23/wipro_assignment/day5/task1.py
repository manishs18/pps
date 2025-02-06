'''
Task 1: Use Python's re module to find all occurrences of the word ""Python"" in a given text.
'''
import re

text = "Python is fun. Python is powerful."
matches = re.findall(r"Python", text)
print("Occurrences of 'Python':", matches)
