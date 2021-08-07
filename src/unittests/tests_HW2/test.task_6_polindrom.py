import ddt
import task_6_polindrom
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
        (111, 111),
        (121, 121),
        (7, 7),
    )
    @ddt.unpack
    def test_polindrom_positive(self, number, expect_num):
        """Проверка яляется ли число полиндромом. Положительный результат"""
        res = task_6_polindrom.my_func_2_6(number)
        self.assertEqual(res, expect_num)

    @ddt.data(
        (123, 123),
        (456, 456),
        (121.5, 121),
    )
    @ddt.unpack
    def test_polindrom_negative(self, number, expect_num):
        """Проверка яляется ли число полиндромом. Отрицательный результат"""
        res = task_6_polindrom.my_func_2_6(number)
        self.assertNotEqual(res, expect_num)

    @ddt.data(
        (3223, 3232)
    )
    @ddt.unpack
    def test_polindrom_count_equal(self, number, compare_num):
        """Проверка: полученное число меньше заданного"""
        res = task_6_polindrom.my_func_2_6(number)
        self.assertLess(res, compare_num, True)

    @ddt.data(
        ('string', TypeError),
        ({122}, TypeError),
    )
    @ddt.unpack
    def test_type_errors(self, word, expected):
        """Проверка ввода данных"""
        with self.assertRaises(expected):
            task_6_polindrom.my_func_2_6(word)


if __name__ == '__main__':
    unittest.main()
