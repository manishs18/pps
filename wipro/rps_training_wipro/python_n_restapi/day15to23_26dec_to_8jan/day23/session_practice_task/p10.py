'''
Hello, Manish
Hello, Manish
Hello, Manish
'''

def repeat(n):
    def decorator(func):

        def wrapper(*args, **kwargs):
            # print(n)
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f'Hello, {name}')


@repeat(1)
def greet2(fname,sname):
    print(f'Hello {fname}{sname}')


d = {'fName':'Manish', 'sName': 'Singh'}
@repeat(1)
def greet3(d):
    print(d)

greet("singh")

greet2("Manish","Singh")

greet3(d)