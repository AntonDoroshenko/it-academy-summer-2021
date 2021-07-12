def get_rangers(my_list):
    """Реализовать функцию get_ranges.

    Реализовать функцию get_ranges которая получает на вход непустой список
    неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
    список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"

    """
    my_list.sort()
    new_list = []
    first_stop_point = int()
    for i in range(len(my_list) - 1):
        if my_list[i + 1] - my_list[i] != 1:
            new_list = f'{my_list[0]}-{my_list[i]}'
            first_stop_point = my_list[i]
            break
    new_list2 = []
    second_stop_point = int()
    for i in range(len(my_list) - 1):
        if my_list[i] > first_stop_point and my_list[i + 1] - my_list[i] == 1:
            new_list2 = f'{my_list[i]}-{my_list[i + 1]}'
            second_stop_point = my_list[i + 1]
    new_list3 = []
    for i in range(len(my_list)):
        if my_list[i] > second_stop_point:
            new_list3 = my_list[i]
    print()
    print(new_list, new_list2, new_list3, sep=',')
    print()


get_rangers([2, 10, 4, 3, 0, 7, 8, 1])


def get_rangers_2(my_list):
    """Реализовать функцию get_ranges_2.

    Реализовать функцию get_ranges которая получает на вход непустой список
    неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
    список “сворачивает”
    get_ranges([4,7,10]) // "4,7,10"

    """
    my_list.sort()
    new_list = []
    for i in range(len(my_list) - 1):
        if my_list[i + 1] - my_list[i] == 3:
            new_list += str(my_list[i])
    new_list.append(str(my_list[-1]))
    print(new_list)
    print()


get_rangers_2([7, 4, 10])


def get_rangers_3(my_list):
    """Реализовать функцию get_ranges_3.

    Реализовать функцию get_ranges которая получает на вход непустой список
    неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
    список “сворачивает”
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"

    """
    my_list.sort()
    new_list = []
    first_stop_point = int()
    for i in range(len(my_list) - 1):
        if my_list[i + 1] - my_list[i] != 1:
            new_list = f'{my_list[0]}-{my_list[i]}'
            first_stop_point = my_list[i]

    new_list2 = []
    for i in range(len(my_list)):
        if my_list[i] > first_stop_point:
            new_list2 = f'{my_list[i]}-{my_list[1 + i]}'
            break
    print(new_list, new_list2, sep=',')


get_rangers_3([3, 8, 2, 9])
