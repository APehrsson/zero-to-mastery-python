import re

pattern = re.compile(r"([A-Za-z0-9@#$%=]{8,}\d)")
password = 'hello2g@'

if pattern.search(password): 
    print('Password validated')
else:
    print('Wrong password format')


#8 char long
#any sort of letters, numbers and $%#@