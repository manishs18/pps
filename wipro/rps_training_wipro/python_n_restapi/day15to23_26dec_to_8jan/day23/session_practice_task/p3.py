class MyIterator:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self


    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        val = self.data[self.index]
        self.index += 1
        return val



class Employee:

    def __init__(self,id=0,name=""):
        self.id = id
        self.name = name

    def disp(self):
        print("="*30)
        print(f"\nEmployee Details\nID: {self.id}\nName: {self.name}")
        print("=" * 30)


e1 = Employee(101,"abc1")
e2 = Employee(102,"abc2")
e3 = Employee(103,"abc3")


try:
    i1 = MyIterator([e1,e2,e3])
    print(i1)
    while(True):
        print(next(i1))

except StopIteration as e:
    print("End of Iterations")

# for val in i1:
#     val.disp()