'''
3. Write a Python function that takes a list of words and returns the length of the longest 
one.
'''

def find_longest_word(words):
    if not words: 
        return 0
    longest_word = max(words, key=len) 
    return len(longest_word)

word_list = list(input("Enter your words within '', separate words: "))
result = find_longest_word(word_list)
print("Length of the longest word:", result)
