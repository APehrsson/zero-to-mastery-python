for item in 'zero to mastery':
    print(item)

for item in [1,2,3,4,5]:
    print(item)


for item in {10}:
    print(item)

for item in (1,2,3,4,5):
    for x in ['a','b','c']:
        print(item, x)

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

for item in user.items():
    print(item)

for item in user.values():
    print(item)

for item in user.keys():
    print(item)
#iterables is a list, dictionary, tuple, set or string. 
#something you can go through one by one.