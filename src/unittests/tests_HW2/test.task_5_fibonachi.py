import task_5_fibonachi
import unittest
import ddt


@ddt.ddt
class TestCase(unittest.TestCase):
    """Выполнить тест домашней задачи

    Оформите указанную задачу из прошлых домашних в виде функции и покройте
    тестами. Учтите, что в функцию могут быть переданы некорректные значения,
    здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию для
    того чтобы она ловила все возможные ситуации сама.

    """

    @ddt.data(
        (5, 3),
        (1, 0),
        (12, 89),
        (100, 218922995834555169026),
    )
    @ddt.unpack
    def test_fib_num_positive(self, number, expect_res):
        """ проверка на положительный результат выполнения программы"""
        res = task_5_fibonachi.my_func_2_5(number)
        self.assertEqual(res, expect_res)

    @ddt.data(
        (5, 5),
        (12, 12),
        (17, 15)
    )
    @ddt.unpack
    def test_fib_num_negative(self, number, expect_res):
        """ проверка на отрицательный результат выполнения программы"""
        res = task_5_fibonachi.my_func_2_5(number)
        self.assertNotEqual(res, expect_res)

    @ddt.data(
        (5, 1),
    )
    @ddt.unpack
    def test_fib_num_type(self, number, expect_res):
        """ проводит сравнение рещзультата программы с заданным числом"""
        res = task_5_fibonachi.my_func_2_5(number)
        self.assertGreater(res, expect_res, True)

    @ddt.data(
        ('string', TypeError),
        ({122}, TypeError),
    )
    @ddt.unpack
    def test_type_errors(self, word, expected):
        """ проверка входящих данных"""
        with self.assertRaises(expected):
            task_5_fibonachi.my_func_2_5(word)


if __name__ == '__main__':
    unittest.main()
