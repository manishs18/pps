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

    if not(len(sys.argv) < 4):
        op = sys.argv[1] #"*"
        op1 = int(sys.argv[2]) #10
        op2 = int(sys.argv[3]) #3

        main(op,op1,op2)
    else:
        print("Usage: python script.py op arg1 arg2")