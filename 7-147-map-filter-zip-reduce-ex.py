from functools import reduce
#Map
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def to_upper(string):
    return string.upper()

print(list(map(to_upper, my_pets)))

#Zip
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, my_numbers[::-1])))

#Filter
scores = [73,20,65,19,76,100,88]
def over_50(score):
    return score > 50

print(list(filter(over_50, scores)))

#Reduce
def accumulater(acc, item):
    return acc + item

print(reduce(accumulater, (my_numbers + scores)))