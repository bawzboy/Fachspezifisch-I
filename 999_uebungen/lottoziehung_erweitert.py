"""
Schreibe ein Programm, mit dem Du Lotto spielen kannst. 6 aus 49.
 
Als Eingabe müssen 6 unterschiedliche Zahlen zwischen 1 und 49 aufgenommen werden. Als siebte Zahl erfolgt dann die Angabe der Superzahl (0 - 9)
 
In einer danach folgenden Schleife sollen per Zufallsgenerator ebenso 6 unterschiedliche(!) Zahlen gezogen und eine Superzahl ermittelt werden. Eine count Variable soll die Anzahl der insgesamten Durchläufe anzeigen.
 
Jede Gewinnkombination soll auf der Konsole ausgegeben werden.
 
Die Schleife ist fertig, wenn 6 Richtige inkl. Superzahl gezogen wurden. Dann die Gewinnkombination ausgeben und die Anzahl der Ziehungen.


Gewinnklassen (Die Ziffer ist die Anzahl der Richtigen. SZ ist die Superzahl)

I    -> 6SZ
II   -> 6
III  -> 5SZ
IV   -> 5
V    -> 4SZ
VI   -> 4
VII  -> 3SZ
VIII -> 3
IX   -> 2SZ   


Bonusmission:
Am Ende des kompletten Durchlaufes soll auch ausgegeben werden, wie oft welche Gewinnkombination gezogen wurde.
"""

from random import randint

def main():
    tipp = lotto_tipp()
    # super_tipp = super_zahl_tipp()
    verlosung = lotto_ziehung()
    # super_zahl = super_zahl_ziehung()
    counter = 0
    while (verlosung != tipp): #  and (super_zahl != super_tipp)
        verlosung = lotto_ziehung()
        # super_zahl = super_zahl_ziehung()
        counter += 1
    print(tipp)
    print(counter, 'Ziehungen')
    
def lotto_ziehung():
    ziehung = []
    while len(ziehung) < 6:        
            zahl = lotto_zahl()
            if zahl not in ziehung:
                ziehung.append(zahl)
    return sorted(ziehung)
    
def lotto_zahl():
    return randint(1, 49)

def super_zahl_ziehung():
    return randint(1, 9)

def lotto_tipp():
    tipp = []
    while len(tipp) < 6:
        zahl = int(input('Ihr Tipp: '))
        if (1 <= zahl <= 49) and (zahl not in tipp):
            tipp.append(zahl)
        else:
            print('Ungültiger Tipp')
    return sorted(tipp)

def super_zahl_tipp():
    tipp = int(input('Superzahl: '))
    if 1 <= tipp <= 9:
        return tipp
    else:
        print('Ungültiger Tipp')

if __name__ == '__main__':
    main()
