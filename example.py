import random

zahl = random.randint(1,101)
tipp = int(input('Errate die Zahl: '))
while  tipp != zahl:
    tipp = int(input('Errate die Zahl: '))
else:
    print('Richtig!')
