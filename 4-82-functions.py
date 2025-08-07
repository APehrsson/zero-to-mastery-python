#parameters

def say_hello(name, age):
    print(f'hello {name}, you are {age} years old.')

#positional arguments
say_hello('Andreas', 35)
say_hello('Hedda', 6)

# keyword argument(bad practice) could come off confusing 
say_hello(age=2, name='Selma')

#Default parameters
def say_hello_default(name='Herman', age=15):
    print(f'hello {name}, you are {age} years old.')

say_hello_default()
say_hello_default('Sniff')
