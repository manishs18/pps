def log(func):
    # @wraps(func)
    def wrapper(*args,**kwargs):
        print(f'Result of {func.__name__} {args} ', end="")
        result = func(*args, **kwargs)
        print(f' = {result}')

        return result
    return wrapper
# @log
def add(x,y):
    return x+y
@log
def sub(x,y):
    return x-y
x=10
y=20
res = add(x,y)
print(f"Result of add {x} + {y} = {res}")

sub(55,40)

@log
def mul(x,y):
    return x*y

mul(3,5)