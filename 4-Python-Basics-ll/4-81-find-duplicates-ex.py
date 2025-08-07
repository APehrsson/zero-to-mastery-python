some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
new_list = []

for char in some_list:
    if some_list.count(char) > 1:
        if char not in new_list:
            new_list.append(char)

print(new_list)
