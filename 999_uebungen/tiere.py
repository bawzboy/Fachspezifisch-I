'''
Schreibt bitte ein kleines Programm.
 
Es soll als abstrakte Oberklasse "Tier" haben. Als Kindklassen Pferd und Maus. 
 
Welche Methoden hat eine Maus, die ein Pferd nicht hat und viseversa

 
Das braucht Ihr, um eine Klasse als abstrakt zu markieren:
 
class Tier(ABC):
'''

from abc import ABC, abstractmethod

class Tier(ABC):
    
    def __init__(self, name, food):
        self.name = name
        self.favorite_food = food

    @abstractmethod
    def make_sound(self):
        pass

    def __str__(self):
        return f'Tier (name: {self.name}, favorite food: {self.favorite_food})'

class Pferd(Tier):
    
    def __init__(self, name, food):
        super().__init__(name, food)

    def make_sound(self):
        print('Hüü')

class Maus(Tier):

    def __init__(self, name, food):
        super().__init__(name, food)

    def make_sound(self):
        print('Quiek')


def main():

    tier1 = Pferd('Pferdinand', 'Stroh')
    print(tier1)

    tier2 = Maus('Mausfred', 'Nüsse')
    print(tier2)

if __name__ == '__main__':
    main()
