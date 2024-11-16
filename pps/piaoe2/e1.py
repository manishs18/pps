#Exercise 1: Accept numbers from a user



class TakeInput:
    def takeInputs(a, b):
        d=0
        e=0
        for i in a:
            d=d+i
            for j in b:
                e=e+j
        print(d*e, end=" ")
    


s = list(map(int, input("Enter numbers for the first list, separated by spaces: ").split()))
v = list(map(int, input("Enter numbers for the second list, separated by spaces: ").split()))

t = TakeInput.takeInputs(s,v)
