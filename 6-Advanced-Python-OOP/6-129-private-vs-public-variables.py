class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old')

player1 = PlayerCharacter('Andy', 35)

#Player1s attributes could easily be overwritten. Too mark a variable that shouldnt be changed, put _ before.
#player1.name = '!!!!'
#player1.speak = 'BOOOO'

player1.speak()