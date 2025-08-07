# map
# map(action, data)
# usefull for iterable tasks

""" def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list """

my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))
print(my_list) # A pure function does not change anything that is outside of the function