user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 20
}

#1 
print('1', user['greet'])

#2
print('2', user.get('age', 55))

#3 is basket/size in user?
print('3', 'basket' in user)
print('3', 'size' in user)

#4 keys/values methods
print('4', 'greet' in user.keys())
print('4', 'hello' in user.values())

#5 print whole dict
print('5', user.items())

#6 Copy dict
user2 = user.copy()
print('6', user)
print('6', user2)

#7 remove specific from dict
print('7', user.pop('greet'))
print('7', user)

#8 update dict
print('8', user.update({'age': 55}))
print('8', user)

#9 Copy dict and clear old
user2 = user.copy()
print('9', user.clear())
print('9', user2)

#10 clear dict
print('10', user.clear())
print('10', user)
