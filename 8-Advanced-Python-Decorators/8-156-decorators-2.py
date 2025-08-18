

def my_decoratrator(func):
    def wrap_function():
        print('*******')
        func()
        print('*******')
    return wrap_function

@my_decoratrator
def hello():
    print('hello')

@my_decoratrator
def bye():
    print('see you later')

hello()
bye()