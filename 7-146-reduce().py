from functools import reduce

my_list = [1,2,3]
def accumulater(acc, item):
    print(acc, item)
    return acc + item


print(reduce(accumulater,my_list, 0))