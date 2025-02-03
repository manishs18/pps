'''
Problem Statement

Write a Python program to generate the next 15 leap years starting from a given year. 
Populate the leap years into a list and display the list.
'''

def find_leap_years(given_year):
    list_of_leap_years = []
    
    year = given_year
    
    while len(list_of_leap_years) < 15:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            list_of_leap_years.append(year)
        year += 1
    
    return list_of_leap_years

list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)