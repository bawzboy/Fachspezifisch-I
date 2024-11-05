from random import randint

class NicerDicer:

    def __init__(self, sides = 6, pips = 0):
        self.sides = sides
        self.pips = pips


    def roll(self):
        rolled = randint(1, self.sides)
        self.pips = rolled
        return rolled


    def get_pips(self):
        return self.pips


    def __str__(self):
        return f'Der Würfel hat {self.sides} Seiten, als letztes wurde eine {self.pips} gewürfet'


def main():
    wuerfel = NicerDicer()
    print(wuerfel)

    print(wuerfel.roll())
    print(wuerfel)


if __name__ == '__main__':
    main()
