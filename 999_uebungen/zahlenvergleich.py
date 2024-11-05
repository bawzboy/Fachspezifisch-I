from random import randint

a = randint(0, 100)
b = randint(0, 100)

print(f'A = {a}\nB = {b}')
if a == b:
    print('A und B sind gleich')
elif a > b:
    print('A ist größer')
elif a < b:
    print('B ist größer')

# print(f'{a} == {b}: {a == b}')
# print(f'{a} != {b}: {a != b}')
