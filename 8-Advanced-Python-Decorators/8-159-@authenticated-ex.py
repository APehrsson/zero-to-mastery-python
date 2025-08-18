user1 = {
    'name': 'Andy',
    'valid': True
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args,**kwargs)
        else:
            print('User is invalid')
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
