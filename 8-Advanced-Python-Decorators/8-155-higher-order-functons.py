#HOC
#A function that recives a function
def greet(func):
    func()

#Or a function that returns a function
def greet2():
    def func():
        return 5
    return func