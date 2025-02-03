
'''
Problem Statement

Write a python program that accepts a text and displays a string 
which contains the word with the largest frequency in the text and the frequency itself separated by a space.

Rules:
1. The word should have the largest frequency.
2. In case multiple words have the same frequency, then choose the word that has the maximum length.

Assumptions:
1. The text has no special characters other than space.
2. The text would begin with a word and there will be only a single space between the words.

Perform case insensitive string comparisons wherever necessary.

Sample Input                                                     Expected Output

"Work like you do not need money love like                       like 3
you have never been hurt and dance 
like no one is watching"

"Courage is not the absence of fear but rather                   fear 2
the judgement that something else is more 
important than fear"

'''

def max_frequency_word_counter(data):
    data = data.lower()

    words = data.split()

    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1

    max_frequency = 0
    result_word = ""
    for word, freq in frequency_dict.items():
        if freq > max_frequency or (freq == max_frequency and len(word) > len(result_word)):
            max_frequency = freq
            result_word = word

    print(result_word, max_frequency)


data1 = "Work like you do not need money love like you have never been hurt and dance like no one is watching"
data2 = "Courage is not the absence of fear but rather the judgement that something else is more important than fear"

max_frequency_word_counter(data1)
max_frequency_word_counter(data2)  