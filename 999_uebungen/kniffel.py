from random import randint

statistic = {}

for i in range(5, 31):
    statistic[i] = 0

for _ in range(1000):
    roll = 0
    for _ in range(5):
        roll += randint(1, 6)

    statistic[roll] += 1

for key, value in statistic.items():
    print(f'{key:02} -> {value * 'x'}')


# from random import randint  # Möglichst kurze Lösung von John und Daniel
# results = [int()] * 26
# for _ in range(1_000):
#      results[sum(randint(1,6) for _ in range(5)) - 5] += 1
# for i in range(len(results)):
#      print(f"{i + 5:0>2d}->{"x" * results[i]}")
