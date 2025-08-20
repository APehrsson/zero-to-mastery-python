while True:
    try:
        age = int(input('What is your age? '))
        10/age
        raise ValueError('hey cut it out') #good if you are creating your own libary to let the user know that what they are doing is wrong
    except ZeroDivisionError:
        print('please enter a number higher than 0')
        break
    else:
        print('thank you!')
    finally: #good for logging ex, something you want to do no matter what happend earlier in the run
        print('ok, i am finally done')
    print('can you hear me')