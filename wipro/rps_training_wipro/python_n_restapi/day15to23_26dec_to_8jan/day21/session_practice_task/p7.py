class Test:

    __count=10

    def __init__(self, a=0,b=0):
        self.__v1 = a
        self.__v2 = b
        self.__count += 1

    def __str__(self):
        return f'\nclassVar: {self.__count}\nv1: {self.__v1}\nv2: {self.__v2}\n'

    def setValues(self,a,b):
        self.__v1 = a
        self.__v2 = b


    @classmethod
    def setClsVar(cls):
        cls.__count +=1


'''
objT = Test(101,102)

print(objT)

# Test.__count = 202 #class var is also now private
# objT.setClsVar()
Test.setClsVar()
print(objT)

# objT.__v1 = 1 # v1 and v2 have now become private vars
# objT.__v2 = 2 # hence you can't access directly outside class
objT.setValues(1,2)

print(objT)
'''
ob1 = Test(1,2)
print(ob1)
ob2 = Test(3,4)
print(ob2)

ob3 = Test(5,6)
print(ob3)

# Test.setClsVar()
# print(ob1,ob2,ob3)