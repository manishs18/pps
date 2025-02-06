a=10
b=1
l1=[1,2,3]
try:
    res = a/b
    del l1

except ZeroDivisionError as e:
    print("Zero Division error: ",e)
except NameError as e:
    print("Unknown Name: ",e)
except Exception as e:
    print("Error occured: ",e)
else:
    print("No Exceptions occured")
    try:
        print(res, l1)
    except Exception as e:
        print("Error",e)

finally:
    print("Always executed")