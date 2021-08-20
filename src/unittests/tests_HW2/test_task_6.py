import ddt
import task_6
import unittest


@ddt.ddt
class TestCase(unittest.TestCase):
    """Выполнить тест домашней задачи

    Оформите указанную задачу из прошлых домашних в виде функции и покройте
    тестами. Учтите, что в функцию могут быть переданы некорректные значения,
    здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию для
    того чтобы она ловила все возможные ситуации сама.

    """
    @ddt.data(
        (111, True),
        (121, True),
        (7, True),
    )
    @ddt.unpack
    def test_polindrom_positive(self, number, expect):
        """Проверка яляется ли число полиндромом. Положительный результат"""
        res = task_6.my_func_2_6(number)
        self.assertTrue(res, expect)

    @ddt.data(
        (321, False),
        (221, False),
        (725, False),
    )
    @ddt.unpack
    def test_polindrom_negative(self, number, expect):
        """Проверка яляется ли число полиндромом. Положительный результат"""
        res = task_6.my_func_2_6(number)
        self.assertTrue(res, expect)

    @ddt.data(
        (3223, 3232)
    )
    @ddt.unpack
    def test_polindrom_count_equal(self, number, compare_num):
        """Проверка: полученное число меньше заданного"""
        res = task_6.my_func_2_6(number)
        self.assertLess(res, compare_num, True)

    @ddt.data(
        ('string', TypeError),
        ({122}, TypeError),
        (None, TypeError),
    )
    @ddt.unpack
    def test_type_errors(self, word, expected):
        """Проверка ввода данных"""
        with self.assertRaises(expected):
            task_6.my_func_2_6(word)


if __name__ == '__main__':
    unittest.main()
