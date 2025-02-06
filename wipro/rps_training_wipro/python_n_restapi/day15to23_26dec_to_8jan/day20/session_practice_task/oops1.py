#empty class
class Employee:
    '''
    def __init__(self,id,name,sal):
        self.empId = id
        self.empName=name
        self.empSal = sal
'''
    def __init__(self):
        self.empId = 0
        self.empName=""
        self.empSal = 0
    def disp(self):
        print("Employee Details are")
        print(self.empId)
        print(self.empName)
        print(self.empSal)

'''
e1 = Employee(10,"manish",10000)

e1.disp()
e2 = Employee(101,"rk",10001)
e2.disp()
'''
Employee.empName = "Kumar"

e3 = Employee()
e3.disp()




