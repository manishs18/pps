#Exercise 7: Find the number of occurrences of a substring in a string

class Substring:
    def __init__(self,a):
        print("Given String value is: ", a)
        self.count = 0
        for i in range(len(a)-3):
            if a[i: i + 4] == 'ogmt':
                self.count = self.count + 1
        
a1 = input("Enter line Sentence to find substring: ")
a2 = Substring(a1)
print("ogmt appeared: ", a2.count, "times")
