i = 0
while i < 50:
    i = i+1
    print(i)
else:
    print('done with all the work')


my_list = [1,2,3]
for item in my_list:
    print(item)

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

while True:
    response = input('Say something: ')
    if (response == 'bye'):
        break
    