#formatted strings

name = 'Andreas'
age = 35

print('Hi' + ' ' + name + '. You are ' + str(age) + ' years old')

print(f'Hi {name}. You are {age} years old')

print('Hi {}. You are {} years old'.format('Andreas', '35'))

print('Hi {}. You are {} years old'.format(name, age))

print('Hi {1}. You are {0} years old'.format(name, age))

