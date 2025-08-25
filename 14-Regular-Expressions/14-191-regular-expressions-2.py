import re


pattern = re.compile(r"([a-zA-Z]).([a])")
string = 'search the inside of this text please'

a = pattern.search(string) 
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a)
print(b)
print(c)
print(d)
print(a.group(1))
print(a.group(2))