'''
Baue eine Rundungsfunktion
1. Default Rundung
2. Rundungsgenauigkeit als Parameter
'''

# zahl = float(input('Zahl: '))
# stellen = int(input('Wie viele Stellen? '))


def runde_zahl(zahl: int, rundungsstelle: int):
    zahl = str(zahl)
    if int(zahl[rundungsstelle + 1]) > 5:
        zahl[rundungsstelle] += 1
    return int(zahl)


# runde_zahl(31337, 3)

# brauche rundungstelle + stelle dahinter
# if stelle dahinter > 5: rundungsstelle +1
# else rundungsstelle = rundungsstelle
