import sys
try:
    f1 = open(sys.argv[1],"r")
    f2 = open(sys.argv[2],"w")
    ct = f1.read()
    f2.write(ct)
except FileNotFoundError as e:
    print("Error: ",e)
    sys.exit(1)
else:
    f1.close()
    f2.close()