class A:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        print("Cnstr A")
    def __str__(self):
        return (f'x={self.x}\ty={self.y}\n')

    def dispA(self):
        # print(f'x={self.x}\ty={self.y}\n')
        print("Class A")
    def additionA(self):
        return (self.x+self.y)

class B(A):
    def __init__(self,a=0,b=0):
        self.a = a
        self.b = b
        print("Cnstr B")

    def __str__(self):
        return (f'a={self.a}\tb={self.b}\n')

    def dispB(self):
        # print((f'x={self.x}\ty={self.y}\n'))
        self.dispA()
        # print(f'a={self.a}\tb={self.b}\n')
        print("Class B")

    def additionB(self):
        return (self.a+self.b)



objA = A()
objB = B(44,55)

objB.dispB()
