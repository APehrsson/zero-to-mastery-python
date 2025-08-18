def my_decoratrator(func):
    def wrap_function(*args, **kwargs):
        print('*******')
        func(*args, **kwargs)
        print('*******')
    return wrap_function

@my_decoratrator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('Hello')
