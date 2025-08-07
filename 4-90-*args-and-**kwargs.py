# *args and **kwargs

def super_func(*args, **kwargs):
    total = 0
    print(kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total
#                 args         kwargs        
print(super_func(1,2,3,4,5, num1=5, num2=10))