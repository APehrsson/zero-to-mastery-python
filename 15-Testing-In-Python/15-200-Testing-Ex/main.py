import random

def guessing_game(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print(f'Congratulations, the right answer was {answer}!')
            return True
    else:
        print('Hey, I said a number between 1 and 10: ')
        
answer = random.randint(1,10)
while True:
    try:
        guess = int(input('Guess a number between 1-10: '))
        if (guessing_game(guess, answer)):
            break
    except ValueError:
        print('Please enter a number')
        continue
            
