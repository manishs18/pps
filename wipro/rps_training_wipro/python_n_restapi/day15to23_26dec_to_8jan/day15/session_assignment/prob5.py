'''
Q5. Reverse a given num
     i/p
	num 12345
     o/p
     num 54321

'''

num = list(int(input("Enter a number: ")))

reversed_num = 0

while num > 0:
    digit = num % 10 
    reversed_num = reversed_num * 10 + digit  
    num = num // 10 

print("Reversed number:", reversed_num)

