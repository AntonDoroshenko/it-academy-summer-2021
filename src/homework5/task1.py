# Делал три отдельных функции ( runner_a, runner_b, runner_c)
# для трех условий указанных в задаче. В строках документации указал за что
# отвечает каждая из функций.
def runner_a():
    """Runner A. Запускает все функции по очереди.

    Оформите решение задач из прошлых домашних работ в функции.
    Напишите функцию runner. (все станет проще когда мы изучим модули,
    getattr и setattr).
    a - runner() – все фукнции вызываются по очереди
    b - runner(‘func_name’) – вызывается только функцию func_name.
    c - runner(‘func’, ‘func1’...) - вызывает все переданные функции

    """
    def my_func_2_1(rub, penny, count):
        """Напишите программу, которая считает общую цену.

        Вводится M рублей и N копеек цена, а также количество S товара.
        Посчитайте общую цену в рублях и копейках за L товаров.
        Пример:
        Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
        Output: Общая цена 9 рублей 60 копеек.

        """
        price = (rub * 100 + penny) * count
        price_rub = price // 100
        price_pen = price % 100
        print('Общая стоимость: ', str(price_rub) + ' руб.',
              str(price_pen) + ' коп.')

    my_func_2_1(3, 20, 3)

    def my_func_2_2(sentence):
        """Найти самое длинное слово в введенном предложении.

        Учтите что в предложении есть знаки препинания.
        Подсказки:
        - my_string.split([chars]) возвращает список строк.
        - len(list) - количество элементов в списке.

        """
        for i in (',', '.', '!', '?', ':', ';'):
            sentence = sentence.replace(i, '')
        sentence = sentence.split()
        long_word = max(sentence, key=len)
        print(long_word)

    my_func_2_2(input('Введите предложение: '))

    def my_func_2_3(list_):
        """Вводится строка.

        Требуется удалить из нее повторяющиеся символы и все пробелы.
        Например, если было введено "abc cde def",то должно быть выведено
        "abcdef".

        """
        del_probel = list_.replace(" ", "")
        short_list = ''
        for i in del_probel:
            if i not in short_list:
                short_list += i
        print(short_list)

    my_func_2_3(input('Введите строку: '))

    def my_func_2_4(list_, small_symbol, big_symbol):
        """Посчитать количество букв.

        Посчтитаь количество строчных (маленьких) и прописных (больших) букв в
        введенной строке. Учитывать только английские буквы.

        """
        for i in list_:
            if "a" <= i <= "z":
                small_symbol += 1
            else:
                if "A" <= i <= "Z":
                    big_symbol += 1
        print("Количество малых букв ---> ", small_symbol)
        print("Количество больших букв ---> ", big_symbol)

    my_func_2_4((input('Введите новую строку: ')), 0, 0)

    def my_func_2_5(number, fib_1, fib_2, i):
        """Числа Фибоначчи.

        Выведите n-ое число Фибоначчи, используя только временные переменные,
        циклические операторы и условные операторы. n - вводится.

        """
        if i != number:
            while i < number:
                fib_1, fib_2 = fib_2, fib_1 + fib_2
                i += 1
        print('Число Фибоначчи это ---> ', fib_1)

    my_func_2_5((int(input('Введите n-е число: '))), 0, 1, 1)

    def my_func_2_6(n1, n2):
        """Палиндром.

        Определите, является ли число палиндромом (читается слева направо и
        справа налево одинаково). Число положительное целое, произвольной
        длины.Задача требует работать только с числами (без конвертации числа
        в строку или что-нибудь еще)

        """
        b = n1
        while n1 > 0:
            # находим остаток - последнюю цифру
            digit = n1 % 10
            # делим нацело - удаляем последнюю цифру
            n1 = n1 // 10
            # увеличиваем разрядность второго числа
            n2 = n2 * 10
            # добавляем очередную цифру
            n2 = n2 + digit
        print('"Обратное" ему число:', n2)
        if b == n2:
            print('Палиндром')
        else:
            print('Не палиндром')

    my_func_2_6((int(input('Введите число: '))), 0)

    def my_func_2_7(a, b, c):
        """Задача про треугольник.

        Даны: три стороны треугольника. Требуется: проверить, действительно ли
        это стороны треугольника. Если стороны определяют треугольник, найти
        его площадь. Если нет, вывести сообщение о неверных данных.

        """
        if a + b > c and a + c > b and b + c > a:
            print("Треугольник существует")
        else:
            print("Треугольник не существует")

    my_func_2_7(
        (int(input('a = '))),
        (int(input('b = '))),
        (int(input('c = ')))
    )

    def my_func_2_8_1(a, b):
        """Открытая задача.

        Зарегистрируйтесь на одном (или нескольких) из сайтов:
        https://py.checkio.org/ , https://www.codewars.com, https://acmp.ru
        https://www.hackerrank.com/ и решите 1-5 задач уровня Elementary и
        advanced. Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул
        реквест

        """
        # your code here
        return a * b

    if __name__ == '__main__':
        print("Example:")
        print(my_func_2_8_1(3, 2))

    def my_func_2_8_2(text: str) -> str:

        # your code here
        return text.split()[0]

    if __name__ == '__main__':
        print("Example:")
        print(my_func_2_8_2("Hello world"))

    def my_func_2_8_3(password: str) -> bool:
        return len(password) > 6

    if __name__ == '__main__':
        print("Example:")
        print(my_func_2_8_3('short'))

    def my_func_2_8_4(val: str) -> str:
        return val[::-1]

    if __name__ == '__main__':
        print("Example:")
        print(my_func_2_8_4('val'))

    def my_func_2_8_5(a: int) -> int:
        # your code here
        return len(str(a))

    if __name__ == '__main__':
        print("Example:")
        print(my_func_2_8_5(10))

    def my_func_3_1(a, b):
        """FizzBuz.

        Напишите программу, которая печатает цифры от 1 до 100, но
        вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
        а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

        """
        for i in range(a, b):
            if i % 3 == 0:
                print('Fizz')
            if i % 5 == 0:
                print('Buzz')
            if i % 5 == 0 and i % 3 == 0:
                print('FizzBuzz')
            else:
                print(i)

    my_func_3_1(0, 101)

    def my_func_3_2(l_1, l_2, l_3, l_4):
        """List practice.

        Используйте генератор списков чтобы получить следующий:
        ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
        Используйте на предыдущий список slice чтобы получить следующий:
        ['ab', 'ad', 'bc'].
        Используйте генератор списков чтобы получить следующий
        ['1a', '2a', '3a', '4a'].
        Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте
        его.
        Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
        списке этого элемента не было.

        """
        first_lst = [(i + j) for i in l_1 for j in l_2]
        print(first_lst)
        second_lst = first_lst[::2]
        print(second_lst)

        numb_lst = [(i + j) for i in l_3 for j in l_4]
        print(numb_lst)

        print(numb_lst.pop(1))

        final_lst = numb_lst.copy()
        final_lst.insert(1, '2a')
        print(final_lst)

    my_func_3_2(['a', 'b'], ['b', 'c', 'd'], ['1', '2', '3', '4'], ['a'])

    def my_func_3_3(l_1, tpl_1, tpl_2):
        """Tuple practice.

        Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
        Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
        Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
        Создайте кортеж из одного элемента, чтобы при итерировании по этому
        элементу последовательно выводились значения 1, 2, 3.
        Убедитесь что len() исходного кортежа возвращает 1.

        """
        new_tuple = tuple(l_1)
        print(new_tuple)

        nw_lst = list(tpl_1)
        print(nw_lst)

        a, b, c = 'a', 2, 'python'
        print(a, b, c)

        print(len(tpl_2))
        for i in tpl_2[0]:
            print(i, end=' ')

    my_func_3_3(['a', 'b', 'c'], ('a', 'b', 'c'), ([1, 2, 3],))

    def my_func_3_4(str_):
        """Пары элементов.

        Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
        другу.
        Считается, что любые два элемента, равные друг другу образуют
        одну пару, которую необходимо посчитать.
        Входные данные - строка из чисел, разделенная пробелами.
        Выходные данные - количество пар.
        Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.

        """
        lst = str_.split()
        number = 0
        for i in lst:
            while lst.count(i) > 1:
                lst.remove(i)
                number += lst.count(i)
        print(str(number))

    my_func_3_4((input('Введите число ')))

    def my_func_3_5(lst_1, lst_2):
        """Уникальные элементы в списке.

        Дан список. Выведите те его элементы, которые встречаются в списке
        только один раз.
        Элементы нужно выводить в том порядке, в котором они встречаются в
        списке.

        """
        for i in lst_1:
            if lst_1.count(i) == 1:
                lst_2 += [i]
        print(lst_2)

    first = [1, 2, 3, 4, 5, 6, 6, 7, 2, 1, 23, 9, 12, 23]
    second = []
    my_func_3_5(first, second)

    def my_func_3_6(new_lstt):
        """Упорядоченный список.

        Дан список целых чисел. Требуется переместить все ненулевые элементы в
        левую часть списка, не меняя их порядок, а все нули - в правую часть.
        Порядок ненулевых элементов изменять нельзя, дополнительный список
        использовать нельзя, задачу нужно выполнить за один проход по списку.
        Распечатайте полученный список.

        """
        for i in new_lstt:
            if i == 0:
                new_lstt.remove(i)
                new_lstt.append(i)
        print(new_lstt)

    new_lst = [1, 3, 4, 10, 23, 0, 0, 7, 5, 8, 0, 8, 7, 0]
    my_func_3_6(new_lst)

    def my_func_4_1(dct_gen):
        """Dict comprehensions.

        Создайте словарь с помощью генератора словарей, так чтобы его ключами
        были числа от 1 до 20, а значениями кубы этих чисел.

        """
        print(dct_gen, type(dct_gen))

    dct_gen = {str(element): element ** 3 for element in range(21)}
    my_func_4_1(dct_gen)

    def my_func_4_2(list_country_and_cities=None, city_search=None):
        """Города

        Дан список стран и городов каждой страны. Затем даны названия городов.
        Для каждого города укажите, в какой стране он находится.
        Входные данные:
        Программа получает на вход количество стран N. Далее идет N строк,
        каждая строка начинается с названия страны, затем идут названия городов
        этой страны.
        В следующей строке записано число M, далее идут M запросов — названия
        каких-то M городов, перечисленных выше.
        Выходные данные:
        Для каждого из запроса выведите название страны, в котором находится
        данный город.

           """
        if city_search is None:
            city_search = ["Minsk", "Odessa"]
        if list_country_and_cities is None:
            list_country_and_cities = [
                "Bel Minsk Baranovichi",
                "Ukraine Kiev Odessa"]
        dict_country_and_cities = {}
        for str_country_and_cities in list_country_and_cities:
            list_cities = []
            str_country_and_cities = str_country_and_cities.split()
            for cities_of_the_country in str_country_and_cities[1:]:
                list_cities.append(cities_of_the_country)
            dict_country_and_cities[str_country_and_cities[0]] = list_cities
        countries = ""
        for i in city_search:
            for country, cities_of_the_country in \
                    dict_country_and_cities.items():
                if i in cities_of_the_country:
                    countries += country + "\n"
        print(countries)

    def my_func_4_3(list_1, list_2):
        """Даны два списка чисел.

        Посчитайте, сколько различных чисел содержится одновременно как в
        первом списке, так и во втором.

        """
        list_3 = set(list_1) | set(list_2)
        print(len(list_3))

    list_1 = ([1, 2, 43, 56, 2, 43, 2, 56, 6, 7])
    list_2 = ([3, 4, 57, 4, 5, 3, 213, 213, 4, 3, 4])
    my_func_4_3(list_1, list_2)

    def my_func_4_4(list_1, list_2):
        """Даны два списка чисел.

        Посчитайте, сколько различных чисел входит только в один из этих
        списков.

        """
        set_1 = set(list_1)
        set_2 = set(list_2)
        end_count = set_1 ^ set_2
        print('Количество чисел ---> ', len(end_count))

    list_1 = ([1, 2, 43, 56, 2, 43, 2, 56, 6, 7])
    list_2 = ([3, 4, 57, 4, 56, 3, 2, 2, 6, 3, 4])
    my_func_4_4(list_1, list_2)

    def my_func_4_5(first_student, second_student, third_student):
        """Языки.

        Каждый из N школьников некоторой школы знает Mi языков.
        Определите, какие языки знают все школьники и языки, которые знает хотя
        бы один из школьников.

        """
        popular_lang = set(
            first_student) & set(second_student) & set(third_student)
        print(len(popular_lang))
        print('Все знают ---> ', list(popular_lang))
        lang_list = set(
            first_student) | set(second_student) | set(third_student)
        print(len(lang_list))
        print('Эти языки знает хотя бы один ученик ---> ', list(lang_list))

    first_student = ['Rus', 'Bel']
    second_student = ['Rus', 'Bel', 'Eng']
    third_student = ['Rus', 'Itl', 'Fr']
    my_func_4_5(first_student, second_student, third_student)

    def my_func_4_6(text):
        """Слова.

        Во входной строке записан текст. Словом считается последовательность
        непробельных символов идущих подряд, слова разделены одним или большим
        числом пробелов или символами конца строки. Определите, сколько
        различных слов содержится в этом тексте.

        """
        for i in ('.', '!', '?'):
            text = text.replace(i, '')
        text = text.split()
        print('Количество различных слов в тексте ---> ', len(set(text)))

    my_func_4_6(input('Введите текст: '))

    def my_func_4_7(num_1, num_2):
        """Оглянемся назад. Числа.

        Даны два натуральных числа. Вычислите их наибольший общий делитель при
        помощи алгоритма Евклида (мы не знаем функции и рекурсию).

        """
        while num_1 != 0 and num_2 != 0:
            if num_1 > num_2:
                num_1 = num_1 % num_2
            else:
                num_2 = num_2 % num_1
        print('НОД указанных чисел ---> ', num_1 + num_2)

    my_func_4_7(381, 645)


runner_a()
print('Runner_A, вызывающий все функции по очереди - завершил работу')


def my_func_2_1():
    """Напишите программу, которая считает общую цену.

    Вводится M рублей и N копеек цена, а также количество S товара.
    Посчитайте общую цену в рублях и копейках за L товаров.
    Пример:
    Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
    Output: Общая цена 9 рублей 60 копеек.

    """
    rub = 3
    penny = 20
    count = 3
    price = (rub * 100 + penny) * count
    price_rub = price // 100
    price_pen = price % 100
    print('Общая стоимость: ', str(price_rub) + ' руб.',
          str(price_pen) + ' коп.')


def my_func_2_2():
    """Найти самое длинное слово в введенном предложении.

    Учтите что в предложении есть знаки препинания.
    Подсказки:
    - my_string.split([chars]) возвращает список строк.
    - len(list) - количество элементов в списке.

    """
    sentence = input('Введите предложение: ')
    for i in (',', '.', '!', '?', ':', ';'):
        sentence = sentence.replace(i, '')
    sentence = sentence.split()
    long_word = max(sentence, key=len)
    print(long_word)


def my_func_2_3():
    """Вводится строка.

    Требуется удалить из нее повторяющиеся символы и все пробелы.
    Например, если было введено "abc cde def",то должно быть выведено "abcdef".

    """
    list_ = input('Введите строку: ')
    del_probel = list_.replace(" ", "")
    short_list = ''
    for i in del_probel:
        if i not in short_list:
            short_list += i
    print(short_list)


def my_func_2_4():
    """Посчитать количество букв.

    Посчтитаь количество строчных (маленьких) и прописных (больших) букв в
    введенной строке. Учитывать только английские буквы.

    """
    small_symbol = 0
    big_symbol = 0
    list_ = input('Введите новую строку: ')
    for i in list_:
        if "a" <= i <= "z":
            small_symbol += 1
        else:
            if "A" <= i <= "Z":
                big_symbol += 1
    print("Количество малых букв ---> ", small_symbol)
    print("Количество больших букв ---> ", big_symbol)


def my_func_2_5():
    """Числа Фибоначчи.

    Выведите n-ое число Фибоначчи, используя только временные переменные,
    циклические операторы и условные операторы. n - вводится.

    """
    number = int(input('Введите n-е число: '))
    fib_1 = 0
    fib_2 = 1
    i = 1
    if i != number:
        while i < number:
            fib_1, fib_2 = fib_2, fib_1 + fib_2
            i += 1
    print('Число Фибоначчи это ---> ', fib_1)


def my_func_2_6():
    """Палиндром.

    Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково). Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)

    """
    n1 = int(input('Введите число: '))
    n2 = 0
    b = n1
    while n1 > 0:
        # находим остаток - последнюю цифру
        digit = n1 % 10
        # делим нацело - удаляем последнюю цифру
        n1 = n1 // 10
        # увеличиваем разрядность второго числа
        n2 = n2 * 10
        # добавляем очередную цифру
        n2 = n2 + digit
    print('"Обратное" ему число:', n2)
    if b == n2:
        print('Палиндром')
    else:
        print('Не палиндром')


def my_func_2_7():
    """Задача про треугольник.

    Даны: три стороны треугольника. Требуется: проверить, действительно ли это
    стороны треугольника. Если стороны определяют треугольник, найти его
    площадь.
    Если нет, вывести сообщение о неверных данных.

    """
    a = int(input('a = '))
    b = int(input('c = '))
    c = int(input('c = '))
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
    else:
        print("Треугольник не существует")


def my_func_2_8_1():
    """Открытая задача.

    Зарегистрируйтесь на одном (или нескольких) из сайтов:
    https://py.checkio.org/ , https://www.codewars.com, https://acmp.ru
    https://www.hackerrank.com/ и решите 1-5 задач уровня Elementary и
    advanced. Поместите 3 простых и 2 сложных задачи на Ваш выбор в пул реквест

    """
    a = 3
    b = 2
    print(a * b)


def my_func_2_8_2():
    # your code here
    text = 'hello world'
    print(text.split()[0])


def my_func_2_8_3():
    word = input('Enter word')
    if len(word) > 6:
        print("Len = ", len(word))
    else:
        print('Not work')


def my_func_2_8_4():
    val = input('Plz enter string')
    print(val[::-1])


def my_func_2_8_5():
    a = 10
    print(len(str(a)))


def my_func_3_1():
    """FizzBuz.

    Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,
    кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел
    одновременно кратных и 3 и 5 - FizzBuzz.

    """
    for i in range(0, 101):
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        elif i % 5 == 0 and i % 3 == 0:
            print('FizzBuzz')
        else:
            print(i)


def my_func_3_2():
    """List practice.

    Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    Используйте на предыдущий список slice чтобы получить следующий:
    ['ab', 'ad', 'bc'].
    Используйте генератор списков чтобы получить следующий
    ['1a', '2a', '3a', '4a'].
    Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
    Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
    списке этого элемента не было.

    """
    l_1 = ['a', 'b']
    l_2 = ['b', 'c', 'd']
    l_3 = ['1', '2', '3', '4']
    l_4 = ['a']
    first_lst = [(i + j) for i in l_1 for j in l_2]
    print(first_lst)
    second_lst = first_lst[::2]
    print(second_lst)

    numb_lst = [(i + j) for i in l_3 for j in l_4]
    print(numb_lst)

    print(numb_lst.pop(1))

    final_lst = numb_lst.copy()
    final_lst.insert(1, '2a')
    print(final_lst)


def my_func_3_3():
    """Tuple practice.

    Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
    Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
    Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
    Создайте кортеж из одного элемента, чтобы при итерировании по этому
    элементу последовательно выводились значения 1, 2, 3.
    Убедитесь что len() исходного кортежа возвращает 1.

    """
    l_1 = ['a', 'b', 'c']
    tpl_1 = ('a', 'b', 'c')
    tpl_2 = ([1, 2, 3],)
    new_tuple = tuple(l_1)
    print(new_tuple)

    nw_lst = list(tpl_1)
    print(nw_lst)

    a, b, c = 'a', 2, 'python'
    print(a, b, c)

    print(len(tpl_2))
    for i in tpl_2[0]:
        print(i, end=' ')


def my_func_3_4():
    """Пары элементов.

    Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг
    другу.
    Считается, что любые два элемента, равные друг другу образуют одну пару,
    которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар.

    """
    str_ = input('Введите число ')
    lst = str_.split()
    number = 0
    for i in lst:
        while lst.count(i) > 1:
            lst.remove(i)
            number += lst.count(i)
    print(str(number))


def my_func_3_5():
    """Уникальные элементы в списке.

    Дан список. Выведите те его элементы, которые встречаются в списке только
    один раз.
    Элементы нужно выводить в том порядке, в котором они встречаются в списке.

    """
    lst_1 = [1, 2, 3, 4, 5, 6, 6, 7, 2, 1, 23, 9, 12, 23]
    lst_2 = []
    for i in lst_1:
        if lst_1.count(i) == 1:
            lst_2 += [i]
    print(lst_2)


def my_func_3_6():
    """Упорядоченный список.

    Дан список целых чисел. Требуется переместить все ненулевые элементы в
    левую часть списка, не меняя их порядок, а все нули - в правую часть.
    Порядок ненулевых элементов изменять нельзя, дополнительный список
    использовать нельзя, задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.

    """
    new_lstt = [1, 3, 4, 10, 23, 0, 0, 7, 5, 8, 0, 8, 7, 0]
    for i in new_lstt:
        if i == 0:
            new_lstt.remove(i)
            new_lstt.append(i)
    print(new_lstt)


def my_func_4_1():
    """Dict comprehensions.

    Создайте словарь с помощью генератора словарей, так чтобы его ключами были
    числа от 1 до 20, а значениями кубы этих чисел.

    """
    dct_gen = {str(element): element ** 3 for element in range(21)}
    print(dct_gen, type(dct_gen))


def my_func_4_2(list_country_and_cities=None, city_search=None):
    """Города

    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    Входные данные:
    Программа получает на вход количество стран N. Далее идет N строк,
    каждая строка начинается с названия страны, затем идут названия городов
    этой страны.
    В следующей строке записано число M, далее идут M запросов — названия
    каких-то M городов, перечисленных выше.
    Выходные данные:
    Для каждого из запроса выведите название страны, в котором находится
    данный город.

       """
    if city_search is None:
        city_search = ["Minsk", "Odessa"]
    if list_country_and_cities is None:
        list_country_and_cities = [
            "Bel Minsk Baranovichi",
            "Ukraine Kiev Odessa"]
    dict_country_and_cities = {}
    for str_country_and_cities in list_country_and_cities:
        list_cities = []
        str_country_and_cities = str_country_and_cities.split()
        for cities_of_the_country in str_country_and_cities[1:]:
            list_cities.append(cities_of_the_country)
        dict_country_and_cities[str_country_and_cities[0]] = list_cities
    countries = ""
    for i in city_search:
        for country, cities_of_the_country in dict_country_and_cities.items():
            if i in cities_of_the_country:
                countries += country + "\n"
    print(countries)


def my_func_4_3():
    """Даны два списка чисел.

    Посчитайте, сколько различных чисел содержится одновременно как в первом
    списке, так и во втором.

    """
    list_1 = ([1, 2, 43, 56, 2, 43, 2, 56, 6, 7])
    list_2 = ([3, 4, 57, 4, 5, 3, 213, 213, 4, 3, 4])
    list_3 = set(list_1) | set(list_2)
    print(len(list_3))


def my_func_4_4():
    """Даны два списка чисел.

    Посчитайте, сколько различных чисел входит только в один из этих списков.

    """
    list_1 = ([1, 2, 43, 56, 2, 43, 2, 56, 6, 7])
    list_2 = ([3, 4, 57, 4, 56, 3, 2, 2, 6, 3, 4])
    set_1 = set(list_1)
    set_2 = set(list_2)
    end_count = set_1 ^ set_2
    print('Количество чисел ---> ', len(end_count))


def my_func_4_5():
    """Языки.

    Каждый из N школьников некоторой школы знает Mi языков. Определите, какие
    языки знают все школьники и языки, которые знает хотя бы один из
    школьников.

    """
    student_counter = 3
    print(student_counter)
    first_student = ['Rus', 'Bel']
    second_student = ['Rus', 'Bel', 'Eng']
    third_student = ['Rus', 'Itl', 'Fr']
    popular_lang = set(
        first_student) & set(second_student) & set(third_student)
    print(len(popular_lang))
    print('Все знают ---> ', list(popular_lang))
    lang_list = set(
        first_student) | set(second_student) | set(third_student)
    print(len(lang_list))
    print('Эти языки знает хотя бы один ученик ---> ', list(lang_list))


def my_func_4_6():
    """Слова.

    Во входной строке записан текст. Словом считается последовательность
    непробельных символов идущих подряд, слова разделены одним или большим
    числом пробелов или символами конца строки. Определите, сколько различных
    слов содержится в этом тексте.

    """
    text = input('Введите текст: ')
    for i in ('.', '!', '?'):
        text = text.replace(i, '')
    text = text.split()
    print('Количество различных слов в тексте ---> ', len(set(text)))


def my_func_4_7():
    """Оглянемся назад. Числа.

    Даны два натуральных числа. Вычислите их наибольший общий делитель при
    помощи алгоритма Евклида (мы не знаем функции и рекурсию).

    """
    num_1 = 381
    num_2 = 645
    while num_1 != 0 and num_2 != 0:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    print('НОД указанных чисел ---> ', num_1 + num_2)


def runner_b(func):
    """Runner B - вызывается только функцию func_name"""
    func()
    print('Выбранная функция завершена')


print('Runner_B - Выполнение выбранной функции по имени: ')
runner_b(my_func_2_1)


def runner_c(*args, **kwargs):
    """Runner C - (‘func’, ‘func1’...) - вызывает все переданные функции."""
    func_one()
    func_two()
    func_three()
    print('Выбранные функции завершили работу')


print('Runner_C - Выполнение выбранных функций по имени')
func_one = my_func_2_1
func_two = my_func_4_7
func_three = my_func_3_6
runner_c(func_one, func_two, func_three)
