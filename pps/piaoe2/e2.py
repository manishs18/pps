#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”

class Display:
    def __init__(self, a):
        result = '**'.join(a.split())
        print(result)
        

s = str(input("Enter The String value: "))
v = Display(s)