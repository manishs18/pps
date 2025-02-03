# def solve(heads,legs):
#     error_msg = 'No Solution'
#     if legs % 2 != 0 or heads > legs / 2 or heads * 4 < legs:
#         return error_msg
#     chicken_count=(legs - 2 * heads) // 2
#     rabbit_count=heads - chicken_count
#     if chicken_count < 0 or rabbit_count < 0:
#         return error_msg
    
#     return chicken_count, rabbit_count
    



# h_inputs = int(input("Enter the head value: "))
# l_inputs = int(input("Enter the head value: "))

# obj = solve(h_inputs, l_inputs)
# print(obj)

# sample_list=["mark",5,"jack",9,"chan",5]

# print(sample_list[::-1])


# def get_count(num_list):
#     count = 0
#     checked = []  

#     for i in range(len(num_list)):
#         if num_list[i] not in checked:
#             occurrence = 0
#             for j in range(len(num_list)):
#                 if num_list[i] == num_list[j]:
#                     occurrence += 1

#             if occurrence > 1:
#                 count += 1
            
#             checked.append(num_list[i])

#     return count

# num_list = [1, 1, 5, 100, -20, -20, 6, 0, 0]
# print(get_count(num_list))

# def ticketGenerated(airline, source, destination, no_of_passengers):
#     tickets = []
    
#     for i in range(1, no_of_passengers + 1):
#         ticket_number = f"{airline[:2].upper()}:{source[:3].upper()}:{destination[:3].upper()}:{100 + i}"
#         tickets.append(ticket_number)
    
#     return tickets[-6:-1]

# airline = input("Enter the Airline: ")
# source = input("Enter the Source Boarding Point: ")
# destination = input("Enter Destination Departing Point: ")
# no_of_passengers = int(input("Enter total number of passengers: "))

# tickets = ticketGenerated(airline, source, destination, no_of_passengers)


# print("Generated Tickets:")
# print(tickets)


'''
1. Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: 
hello world! 123 
Then, the output should be: 
LETTERS 10 
DIGITS 3
'''
user_input  = input("""Enter the Sentences: """)
letters = 0
digits = 0

for i in user_input:
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        letters += 1
    elif i.isdigit():
        digits += 1

print(user_input)
print(letters)
print(digits)