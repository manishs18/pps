'''
Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.
Write a python function which performs the run length encoding for a given String and returns the run length encoded String.
Provide different String values and test your program

Sample Input            Expected Output

AAAABBBBCCCCCCCC        4A4B8C
AABCCA                  2A1B2C1A

'''

# def encode(message):
#     encoded_message = ""
#     count = 1
    
#     for i in range(1, len(message)):
#         if message[i] == message[i - 1]:
#             count += 1
#         else:
#             encoded_message += str(count) + message[i - 1]
#             count = 1
    
#     encoded_message += str(count) + message[-1]
    
#     return encoded_message

# print(encode("AAAABBBBCCCCCCCC")) 
# print(encode("AABCCA"))            
# print(encode("ABBBBCCCCCCCCAB"))   

def findRept(my_str):
    str_len =""
    count = 1
    for i in range(1,len(my_str)):
        if my_str[i] == my_str[i-1]:
            count += 1
        else:
            str_len += str(count) + my_str(i-1)
            count = 1
    str_len += str(count) + my_str[-1]
    return str_len


user_input = "AAAABBBBCCCCCCCC"

print(findRept(user_input))