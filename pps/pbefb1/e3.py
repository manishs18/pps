#Exercise 3: Print characters present at an even index number
# def char_at_even_index(a):

#     e_num = []
#     for i in range(a):
#         if i%2 == 0:
#             e_num = e_num + i
#     return e_num

# s1 = int(input("Enter String: "))
# print(f"original string: {s1}")

# s2=char_at_even_index(s1)
# print(s2)

word = input("Enter word: ")
print("original word: ", word)

size = len(word)
print("Printing only even index chars")
for i in range(0, size -1, 2):
#or
# x = list(word)
# for i in x[0::2]:
    print("index[", i, "]", word[i])

