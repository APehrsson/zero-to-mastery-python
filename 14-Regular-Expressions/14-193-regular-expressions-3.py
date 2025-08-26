import re


pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'

a = pattern.search(string) 
print(a)

#8 char long
#any sort of letters, numbers and $%#@