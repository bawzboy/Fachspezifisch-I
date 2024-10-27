# 1.

# a)

umrechnungsfaktor = 1.95583

# def euro_in_dm():

#     eingabe_wert = float(input('Euro: '))
#     eingabe_wert *= umrechnungsfaktor
#     print(eingabe_wert, 'DM')


def euro_in_dm(eingabe_wert: float):

    eingabe_wert *= umrechnungsfaktor
    return round(eingabe_wert, 2)


def dm_in_euro(eingabe_wert: float):

    eingabe_wert /= umrechnungsfaktor
    return round(eingabe_wert, 2)


# b)
# DM-Eingabe ist das Problem
# Bedienung ohne DM-Eingabe

# Frage: Methode a) zur Umwandlung Euro in DM, Kundin versucht DM in Euro?

# c)
# Ich würde das Eingabefeld DAU(Layer8)-sicher gestalten, um Fehler abzufangen, bevor sie passieren können.

# d)

# def euro_in_dm():

#     try:
#         eingabe_wert = float(input('Euro: '))
#         eingabe_wert *= umrechnungsfaktor
#         print(eingabe_wert, 'DM')
#     except ValueError:
#         print('Bitte nur einen Eurobetrag im Format "123.45" eingeben')

# e)

def eingabe_verarbeitung():

    betrag, waehrung = input('Was soll umgerechnet werden? ').split()
    return (float(betrag), waehrung)

# f)

def umrechnung(eingabe: tuple):
    if eingabe[1] == 'EUR':
        return euro_in_dm(eingabe[0]), 'DM'
    if eingabe[1] == 'DM':
        return dm_in_euro(eingabe[0]), 'EUR'

# print(umrechnung(eingabe_verarbeitung()))

# g)

import sys

if sys.argv[2] == 'EUR':
    print(euro_in_dm(float(sys.argv[1])), 'DM')
if sys.argv[2] == 'DM':
    print(dm_in_euro(float(sys.argv[1])), 'EUR')
