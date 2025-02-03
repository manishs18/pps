'''
Exercise on Recursion in Python - Level 2

Problem Statement

Consider that the human tower is to be performed on a stage and the stage has a maximum weight limit.
Write a python program to find the maximum number of people at the 
base level such that the total weight of tower does not exceed the maximum weight limit of the stage.

Assume that:
1. Each person weighs 50 kg
2. There will always be odd number of men at the base level of the human tower.

'''


def calculate_tower_weight(people_at_base):

    if people_at_base <= 0: 
        return 0

    return people_at_base * 50 + calculate_tower_weight(people_at_base - 2)

def find_max_base_people(max_weight):
    people_at_base = 1
    while True:
        total_weight = calculate_tower_weight(people_at_base)
        if total_weight > max_weight:
            return people_at_base - 2
        
        people_at_base += 2

max_weight_limit = 1000  
max_people_at_base = find_max_base_people(max_weight_limit)
print(f"The maximum number of people at the base level is: {max_people_at_base}")
