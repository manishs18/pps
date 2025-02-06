import sys
def add(a,b):
    return a+b

def mul(a,b):
    return a*b

def main(op,op1,op2):

    if (op == '*'):
        print("Multiplication: ",mul(op1,op2))
    elif (op == '+'):
        print("Addition: ",add(op1,op2))
    else:
        print("Wrong operator")

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: python script.py op arg1 arg2")
        sys.exit(1)
    try:
        op = sys.argv[1] #"*"
        op1 = int(sys.argv[2]) #10
        op2 = int(sys.argv[3]) #3
        main(op,op1,op2)
    except ValueError as e:
        print("Error: ",e)
        print("Usage: python script.py op arg1 arg2")
