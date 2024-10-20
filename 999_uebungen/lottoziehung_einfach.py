"""
Lotto 6 aus 49

Schreibe ein Programm, das 6 unterschiedliche Zufallszahlen zwischen 1 und 49 zieht.

Gebe die Zahlen aus, sobald 6 unterschiedliche Zahlen vorhanden sind

"""

from random import shuffle

def main():
    lotto_topf = list(range(1, 50))
    shuffle(lotto_topf)
    lotto_ziehung = lotto_topf[:6]

    print(sorted(lotto_ziehung))

if __name__ == '__main__':
    main()
