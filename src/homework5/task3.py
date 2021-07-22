def get_ranges(my_list):
    """Реализовать функцию get_ranges.

    Реализовать функцию get_ranges которая получает на вход непустой список
    неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
    список “сворачивает”
    get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
    get_ranges([4,7,10]) // "4,7,10"
    get_ranges([2, 3, 8, 9]) // "2-3,8-9"

    """
    start_list = [my_list[0]]
    for i in my_list[1:]:
        if i - start_list[-1] == 1:
            start_list.append(i)
        else:
            if start_list[0] == start_list[-1]:
                print(str(start_list[0]), end=', ')
            else:
                print(str(start_list[0]) + '-' + str(start_list[-1]), end=', ')
            start_list.clear()
            start_list.append(i)
    if start_list[0] == start_list[-1]:
        print(str(start_list[0]))
    else:
        print(str(start_list[0]) + '-' + str(start_list[-1]))


get_ranges([0, 1, 2, 3, 4, 7, 8, 10])
get_ranges([4, 7, 10])
get_ranges([2, 3, 8, 9])
