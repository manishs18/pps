class Employee:
    #class valriable are decalrred
    compName = "Wipro"
    def __init__(self,id=0,name="",sal=0):
        self.empId = id
        self.empName=name
        self.empSal = sal

    def getName(self):
        return self.empName
    def getId(self):
        return self.empId
    def getSal(self):
        return self.empSal

    def setName(self,name):
        self.empName = name

    def setSal(self, sal):
        self.empSal = sal

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

    @classmethod
    def setCompName(cls, compName):
        '''
        compName
        1. is starting with a numeric char
        2. sp chars
        3. strip string
        '''
        cls.compName = compName




def getEmpDetails(n):
    for i in range(n):
        print(f"Enter Details of {i + 1} Employee")
        name = input("Name: ")
        id = int(input("ID: "))
        sal = int(input("Salary: "))
        objEmp = Employee(id, name, sal)
        e.append(objEmp)
        print("=" * 30)

def printDetEmp(n):
    # display employee details
    for i in range(n):
        e[i].disp()


def updateCDet(n):
    for i in range(n):
        e[i].setCompName(input("Company Name: "))

def updateDetails(n):
    # empId == 2 => empName = 'xyz'
    # print(e[0].getId())
    for i in range(n):
        if e[i].getId() == 2:
            e[i].setName("xyz")

def main(n):
    getEmpDetails(n)
    printDetEmp(n)
    # updateDetails(n)
    updateCDet(n)
    printDetEmp(n)


e = []
'''
e1 = Employee()
e2 = Employee()

e[0] = e1
e[1] = e2
'''
if __name__ == "__main__":
    n = int(input("How many Employee are present: "))

    main(n)

