'''
Task 1: Write a Python program to read a file and print its content line by line.
'''
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
