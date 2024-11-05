def spaceship(a: int|float, b: int|float) -> int:

    if (a - b) < 0:
        return -1
    if (a - b) > 0:
        return 1
    if (a - b) == 0:
        return 0

print(spaceship(42, 73))
print(spaceship(73, 73))
print(spaceship(54, 42))
