from collections import Counter, defaultdict, OrderedDict

list = [1,2,3,4,5,6,7,7]
print(Counter(list))

sentence = 'bla bla bla thinking about python'
print(Counter(sentence))

dictionary = defaultdict(lambda: 'key does not exist',{'a': 1, 'b': 2}) #defaultdict defaults what you choose when a key that doesn't exist is given
print(dictionary['a'])
print(dictionary['b'])
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 1
d2['b'] = 2

print(d2 == d)