
while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('please enter a number')
    except ZeroDivisionError:
        print('please enter a number higher than 0')
    else:
        print('thank you!')
        break