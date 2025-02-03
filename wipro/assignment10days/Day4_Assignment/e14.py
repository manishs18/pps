'''
14. Write a Python program that accepts a comma separated sequence of words as input 
and prints the unique words in sorted form (alphanumerically) 
'''

def sort_unique_words():
    user_input = input("Enter comma-separated words: ")
    words = user_input.split(",")
    unique_words = sorted(set(words))
    print(", ".join(unique_words))

sort_unique_words()
