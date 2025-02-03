'''
Problem Statement

Write python function, sms_encoding() which accepts a sentence and converts it into an abbreviated sentence to be sent as SMS and returns the abbreviated sentence.

Rules are as follows:
a. Spaces are to be retained as is
b. Each word should be encoded separately

If a word has only vowels then retain the word as is
If a word has a consonant (at least 1) then retain only those consonants
Note: Assume that the sentence would begin with a word and there will be only a single space between the words.

Sample Input                                          Expected Output

I love Python                                         I Iv Pythn
MSD says I love cricket and tennis too                MSD sys I lv crckt nd tons t
I will not repeat mistakes                            wll nt rpt mstks

'''


def sms_encoding(data):
    vowels = "aeiouAEIOU"
    result = []

    words = data.split()

    for word in words:
        if all(char in vowels for char in word):
            result.append(word)
        else:
            consonants = "".join(char for char in word if char not in vowels)
            result.append(consonants)

    return " ".join(result)


data1 = "I love Python"
data2 = "MSD says I love cricket and tennis too"
data3 = "I will not repeat mistakes"

print(sms_encoding(data1))
print(sms_encoding(data2)) 
print(sms_encoding(data3)) 