# Scope - What variables do i have access to?
a = 1

def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(a)
print(parent())

print(parent())
print(a)

#1 - start with local ( inside function)
#2 - parent local? (checks if there is an parent function)
#3 - Global
#4 - built in python functions
