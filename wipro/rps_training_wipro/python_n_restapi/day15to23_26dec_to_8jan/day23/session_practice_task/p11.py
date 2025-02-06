'''
class based decorators
'''

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Class based decorator is working")
        return self.func(*args,**kwargs)

@MyDecorator
def say_goodbye():
    print("GoodBye!")

say_goodbye()