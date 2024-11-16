#Exercise 4: Remove first n characters from a string
word = input("Enter Word: ")

def removeChars(word, n):
    print("Original Word: ", word)
    x = word[n:]
    return x

print("Removing characters from a string")
print("after index removed string", removeChars("ogmt", 2))