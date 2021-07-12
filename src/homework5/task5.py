def nearest_degree(number):
    """Найти степень.

    Написать программу которая находит ближайшую степень двойки к введенному
    числу. Например: 10(8), 20(16), 1(1), 13(16)

    """
    degree = 1
    while number >= 2**degree:
        degree += 1
    if number - 2**degree > 2**(degree-1) - number:
        print(f'Ближайшая степень 2 к числу {number} ---> ', 2**degree)
    else:
        print(f'Ближайшая степень 2 к числу {number} ---> ', 2**(degree-1))


nearest_degree(10)
print()
nearest_degree(20)
print()
nearest_degree(1)
print()
nearest_degree(13)
