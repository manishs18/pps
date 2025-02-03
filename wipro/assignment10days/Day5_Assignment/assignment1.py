'''
Write a python function, find_correct() which accepts a dictionary and returns a list as per the rules mentioned below. 
The input dictionary will contain correct spelling of a word as key and the spelling provided by a contestant as the value.
The function should identify the degree of correctness as mentioned below:
CORRECT, if it is an exact match
ALMOST CORRECT, if no more than 2 letters are wrong
WRONG, if more than 2 letters are wrong or if length (correct spelling versus spelling given by contestant) mismatches.
and return a list containing the number of CORRECT answers, number of ALMOST CORRECT answers and number of WRONG answers.

Assume that the words contain only uppercase letters and the maximum word length is 10.
Sample Input                         Expected Output
{"THEIR": "THEIR",                   [2, 2, 1]
 "BUSINESS": "BISINESS", 
 "WINDOWS":
"WINDMILL",
"WERE":"WEAR",
"SAMPLE":"SAMPLE"}
'''

def find_correct(word_dict):
    total_match = [0, 0, 0]  

    for k, v in word_dict.items():
        if k == v:  
            total_match[0] += 1 
        elif len(k) != len(v): 
            total_match[2] += 1  
        else:  
            
            differences = 0
            for i in range(len(k)):
                if k[i] != v[i]:
                    differences += 1
            
            if differences <= 2:
                total_match[1] += 1 
            else:
                total_match[2] += 1 

    return total_match


word_dict = {
    "THEIR": "THEIR", 
    "BUSINESS": "BISINESS", 
    "WINDOWS": "WINMILL", 
    "WERE": "WEAR", 
    "SAMPLE": "SAMPLE"
}

objl1 = find_correct(word_dict)
print(objl1)