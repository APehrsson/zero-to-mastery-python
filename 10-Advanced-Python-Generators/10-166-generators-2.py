def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(10)
next(g)
next(g)
next(g)
print(next(g))
