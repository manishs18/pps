'''
2.  Write a Python program to add 'ing' at the end of a given string (length should be at 
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string 
length 
the 
Sample 
Expected 
Sample 
given string is less than 3, leave it unchanged. 
String 
Result 
String 
Expected Result : 'stringly' 
'''

def modify_string(s):
    if len(s) < 3:  
        return s
    elif s.endswith('ing'):  
        return s + 'ly'
    else:  
        return s + 'ing'

sample_string = input("Enter a string: ")
result = modify_string(sample_string)
print("Modified String:", result)
