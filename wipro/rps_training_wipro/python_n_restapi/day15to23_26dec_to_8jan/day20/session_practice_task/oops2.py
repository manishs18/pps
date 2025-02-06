class Employee:
    #class valriable are decalrred
    compName = "Wipro"
    def __init__(self):
        self.empId = 0
        self.empName=""
        self.empSal = 0

    def setValue(self,id,name,sal):
        self.empId = id
        self.empName = name
        self.empSal = sal
    def disp(self):
        print("Employee Details are")
        print(self.empId)
        print(self.empName)
        print(self.empSal)
        print(self.compName)

e1 = Employee()
e1.disp()
e1.setValue(101,"manish",10001)
e1.disp()

e2 = Employee()
e2.disp()

Employee.compName = "XYZ"
e3 = Employee()
e3.disp()
e1.disp()
e2.disp()

e3.compName = "ABC"
e3.disp()
e1.disp()
e2.disp()

