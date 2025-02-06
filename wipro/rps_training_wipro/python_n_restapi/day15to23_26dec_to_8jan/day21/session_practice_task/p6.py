class Test:

    count=10
    def __init__(self, a=0,b=0):
        self.v1 = a
        self.v2 = b


    def __str__(self):
        return f'\nclassVar: {self.count}\nv1: {self.v1}\nv2: {self.v2}\n'


objT = Test(101,102)

print(objT)

Test.count = 202
print(objT)

objT.v1 = 1
objT.v2 = 2

print(objT)
