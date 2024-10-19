"""
Lotto 6 aus 49

Schreibe ein Programm, das 6 unterschiedliche Zufallszahlen zwischen 1 und 49 zieht.

Gebe die Zahlen aus, sobald 6 unterschiedliche Zahlen vorhanden sind

"""

from random import randint

def main():
    lotto_topf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    
    lotto_ziehung = []
    while len(lotto_ziehung) < 6:
            zahl = randint(1, 49)
            if zahl in lotto_topf and zahl not in lotto_ziehung:
                lotto_ziehung.append(zahl)
    print(sorted(lotto_ziehung))

if __name__ == '__main__':
    main()
