#Set
my_list2 = {char for char in 'hello'}
print(my_list2)

my_list3 = {num for num in range(0,100)}
print(my_list3)

my_list4 = {num**2 for num in range(0,100)}
print(my_list4)

my_list5 = {num**2 for num in range(0,100) if num % 2 ==0}
print(my_list5)

#dict
simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {k:v**2 for k,v in simple_dict.items() if v%2==0}
print(my_dict)

my_dict2 = {num:num*2 for num in [1,2,3]}
print(my_dict2)