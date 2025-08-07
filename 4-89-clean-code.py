# clean code

#mesy
def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False

print(is_even(50))

#clean
def is_even_clean(num):
    if num % 2 == 0:
        return True
    return False

print(is_even_clean(50))

#cleaner
def is_even_cleaner(num):
    return num % 2 == 0
     

print(is_even_cleaner(50))