#OOP, a way to think about and structure code. After making an object you can use it again and again 
#The class is the blueprint. From the blueprint you can create objects over and over. Instances is a created object from a class

class PlayerCharacter:
    # Class Object Attribute (is static, not dynamic)
    membership = True
    def __init__(self, name='Anonymous', age=0):
        if (age > 18):
            self.name = name #attributes
            self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2

player1 = PlayerCharacter('Andreas', 35)
player2 = PlayerCharacter('Emma', 35)
player2.attack = 50

print(player1.shout())
print(player2.name, player2.age)