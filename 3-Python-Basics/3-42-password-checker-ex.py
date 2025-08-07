username = input('Username: ')
password = input('Password: ')

password_length = len(password)

password_encrypted = '*' * password_length

print(f'{username}, your password {password_encrypted} is {password_length} letters long')
