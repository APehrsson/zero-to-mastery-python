import random
import sys

first = int(sys.argv[1])
last = int(sys.argv[2])
number = random.randint(first,last)

while True:
    try:
        guess = int(input(f'Guess a number between {first} and {last}: '))
        if 0 < guess < 11:
            if guess == number:
                print(f'Congratulations, the right answer was {number}!')
                break
        else:
            print(f'Hey, I said a number between {first} and {last}: ')
    except ValueError:
        print('Please enter a number')




    
 
