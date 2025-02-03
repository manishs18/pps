'''
Problem Statement

Care hospital wants to know the medical speciality visited by the maximum number of patients. 
Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. 
The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",

"O":"Orthopedics",

"E":"ENT
}
Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
Note:
1. Assume that there is always only one medical speciality which is visited by maximum number of patients.
2. Perform case sensitive string comparison wherever necessary.

Sample Input                                          Expected Output

[101,P,102,O,302,P,305,P]                             Pediatrics
[101,O,102,O,302,P,305,E,401,O,656,O]                 Orthopedics
[101,O,102,E,302,P,305,P,401,E,656,O,987,E]           ENT

'''

def max_visited_speciality(medical_speciality):
    speciality = {"P": "Pediatrics",
                  "O": "Orthopedics",
                  "E": "ENT"}
    
    p_count = 0
    o_count = 0
    e_count = 0
    
    for v in medical_speciality:
        if v == 'P':
            p_count += 1
        elif v == "O":
            o_count += 1
        elif v == "E":
            e_count += 1
    if p_count > o_count and p_count > e_count:
        return speciality['P']
    elif o_count > p_count and o_count > e_count:
        return speciality['O']
    else:
        return speciality['E']


user_input = [101, 'P', 102, 'O', 302, 'P', 305, 'P']
user_input1 = [101, 'O', 102, 'O', 302, 'P', 305, 'E', 401, 'O', 655,'O']
user_input2 = [101, 'O', 102, 'E', 302, 'P', 305, 'P', 401, 'E', 656, 'O',987,'E']



obj = max_visited_speciality(user_input)
print(obj)

