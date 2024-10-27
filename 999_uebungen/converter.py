import sys


umrechnungsfaktor = 1.95583

def euro_in_dm(eingabe_wert: float):

    eingabe_wert *= umrechnungsfaktor
    return round(eingabe_wert, 2)


def dm_in_euro(eingabe_wert: float):

    eingabe_wert /= umrechnungsfaktor
    return round(eingabe_wert, 2)


if sys.argv[2] == 'EUR':
    print(euro_in_dm(sys.argv[1]))
if sys.argv[2] == 'DM':
    print(dm_in_euro(sys.argv[1]))
