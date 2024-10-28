from random import randint

statistic = {}

for i in range(5, 31):
    statistic[i] = 0

for _ in range(1000):
    roll = 0
    for _ in range(5):
        roll += randint(1, 6)

    if roll in statistic:
        statistic[roll] += 1

for key, value in statistic.items():
    print(f'{key:02d} -> {value * 'x'}')
