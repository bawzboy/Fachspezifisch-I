"""
Lotto 6 aus 49

Schreibe ein Programm, das 6 unterschiedliche Zufallszahlen zwischen 1 und 49 zieht.

Gebe die Zahlen aus, sobald 6 unterschiedliche Zahlen vorhanden sind

"""

from random import randint

def main():
    lotto_ziehung = []
    while len(lotto_ziehung) < 6:        
            zahl = lotto_zahl()
            if zahl not in lotto_ziehung:
                lotto_ziehung.append(zahl)
    print(sorted(lotto_ziehung))


def lotto_zahl():
    return randint(1, 49)

if __name__ == '__main__':
    main()
