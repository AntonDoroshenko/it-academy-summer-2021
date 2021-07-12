def max_del(number):
    """Найти максимальный делитель.

    Вводится число найти его максимальный делитель, являющийся степенью
    двойки. Например 10(2) 16(16), 12(4).

    """
    degree = 1
    while number % 2**degree == 0:
        degree += 1
    print(f'Максимальный делитеь к числу {number} ---> ', 2 ** (degree - 1))


max_del(10)
print()
max_del(16)
print()
max_del(12)
