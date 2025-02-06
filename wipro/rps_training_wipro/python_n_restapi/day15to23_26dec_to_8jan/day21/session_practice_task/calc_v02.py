class calcv02:

    def __init__(self):
        print("calc prg with init method invoked while using")

    @staticmethod
    def add(a, b):
        return (a) + (b)

    @staticmethod
    def sub(a, b):
        return a - b

    def disp(self):
        print("Calculator Program")

if __name__=="__main__":
    obj = calcv02()
    print(obj.add(10,25))
    obj.disp()
