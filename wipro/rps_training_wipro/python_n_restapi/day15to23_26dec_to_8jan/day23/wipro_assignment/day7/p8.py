def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func() #item is wrapped
        print("Something after the function")

    return wrapper

def disp():
    print("Hello World")

def disp1():
    print("My Name is Bhima")

ret = my_decorator(disp) #wrapper address is caugth by ret

ret()
ret = my_decorator(disp1)

ret()