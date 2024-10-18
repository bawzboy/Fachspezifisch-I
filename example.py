import random

def rnd_ganzzahl(start, end):
    return int(random.random() * (end - start + 1) + start)

def rnd_boolean():
    zahl = rnd_ganzzahl(0, 100)
    if zahl % 2 == 0:
        return True
    return False
    
print(rnd_boolean())
