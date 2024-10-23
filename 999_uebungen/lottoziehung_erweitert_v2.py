"""
Schreibe ein Programm, mit dem Du Lotto spielen kannst. 6 aus 49.
 
Als Eingabe müssen 6 unterschiedliche Zahlen zwischen 1 und 49 aufgenommen werden. Als siebte Zahl erfolgt dann die Angabe der Superzahl (0 - 9)
 
In einer danach folgenden Schleife sollen per Zufallsgenerator 6 unterschiedliche(!) Zahlen gezogen und eine Superzahl ermittelt werden. Eine count Variable soll die Anzahl der insgesamten Durchläufe anzeigen.
 
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
from random import shuffle


def main():
    spielschein = spielschein_eingabe()
    ziehung = lotterie()
    gewinnklasse = gewinnklasse_ermitteln_dozent(richtige_zahlen(ziehung, spielschein), 
                                                richtige_superzahl(ziehung, spielschein))

    counter_gesamt, counter_9, counter_8, counter_7, counter_6, counter_5, counter_4, counter_3, counter_2 = 0, 0, 0, 0, 0, 0, 0, 0, 0

    while gewinnklasse != 1:
        ziehung = lotterie()
        counter_gesamt += 1
        print(f'{counter_gesamt:,}')
        if gewinnklasse == 9:
            counter_9 += 1
        elif gewinnklasse == 8:
            counter_8 += 1
        elif gewinnklasse == 7:
            counter_7 += 1
        elif gewinnklasse == 6:
            counter_6 += 1
        elif gewinnklasse == 5:
            counter_5 += 1
        elif gewinnklasse == 4:
            counter_4 += 1
        elif gewinnklasse == 3:
            counter_3 += 1
        elif gewinnklasse == 2:
            counter_2 += 1

    print(f'Jackpot! Gewinnklasse I wurde in {counter_gesamt} Ziehungen erreicht!')
    print(f'Gewinnklasse II wurde {counter_2} gezogen')
    print(f'Gewinnklasse III wurde {counter_3} gezogen')
    print(f'Gewinnklasse IV wurde {counter_4} gezogen')
    print(f'Gewinnklasse V wurde {counter_5} gezogen')
    print(f'Gewinnklasse VI wurde {counter_6} gezogen')
    print(f'Gewinnklasse VII wurde {counter_7} gezogen')
    print(f'Gewinnklasse VIII wurde {counter_8} gezogen')
    print(f'Gewinnklasse IX wurde {counter_9} gezogen')


def spielschein_eingabe():
    spielschein = []

    while len(spielschein) < 6:
        zahl = int(input('Zahl: '))
        if 1<= zahl <= 49 and zahl not in spielschein:
            spielschein.append(zahl)
    superzahl = int(input('Superzahl: '))
    return sorted(spielschein), superzahl


def lotterie():
    lotto_topf = list(range(1, 50))
    shuffle(lotto_topf)
    lotto_ziehung = lotto_topf[:6]
    superzahl = randint(1, 9)
    return sorted(lotto_ziehung), superzahl


def gewinnklasse_ermitteln_dozent(richtige, richtige_sz):
    if richtige < 2 or richtige > 6 or (richtige ==2 and not richtige_sz):
        return 
    return 14 - 2 * richtige - richtige_sz


def gewinnklasse_ermitteln(anz_richtige, superzahl_bool): # return Wert int() casten?
    if anz_richtige == 2 and superzahl_bool is True:
        return 9
    elif anz_richtige == 3 and superzahl_bool is False:
        return 8
    elif anz_richtige == 3 and superzahl_bool is True:
        return 7
    elif anz_richtige == 4 and superzahl_bool is False:
        return 6
    elif anz_richtige == 4 and superzahl_bool is True:
        return 5
    elif anz_richtige == 5 and superzahl_bool is False:
        return 4
    elif anz_richtige == 5 and superzahl_bool is True:
        return 3
    elif anz_richtige == 6 and superzahl_bool is False:
        return 2
    elif anz_richtige == 6 and superzahl_bool is True:
        return 1


def richtige_zahlen(ziehung, spielschein):
    anz_richtige = 0

    for i in range(6):
        for zahl in spielschein[0]:
            if zahl == ziehung[0][i]:
                anz_richtige += 1
    return anz_richtige


def richtige_superzahl(ziehung, spielschein):
    if ziehung[1] == spielschein[1]:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
