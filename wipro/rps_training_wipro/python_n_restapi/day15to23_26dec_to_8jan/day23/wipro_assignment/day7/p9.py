'''
Hello, Bhima
Hello, Bhima
Hello, Bhima
'''

def repeat(n):
    def decorator(func):

        def wrapper(*args, **kwargs):
            # print(n)
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
        # wrapper("Bhima")
        print("Deco is called")
    return decorator


def greet(name):
    print(f'Hello, {name}')

ret = repeat(3) #ret = address of deco
# print(ret)
# decorator(greet)
w = ret(greet)  # w = address of wrapper =>w('args')
w("bhima")