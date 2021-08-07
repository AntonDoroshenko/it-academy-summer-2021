import task_3_different_number
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
        ([1, 2, 43, 56, 2, 43, 2, 56, 6, 7], [3, 4, 57, 4, 5, 3, 213, 4, 3, 4],
         11),
        ([1, 2, 4, 7], [3, 4, 5, 213, 213, 4], 7),
        ([215, 1102, 32], [1102, 32, 455, 567], 5),
    )
    @ddt.unpack
    def test_equal(self, list_1, list_2, expected):
        """Положительный результат выполнения программы"""
        res = task_3_different_number.my_func_4_3(list_1, list_2)
        self.assertEqual(res, expected)

    @ddt.data(
        ([2, 43, 56, 43, 6, 7], [4, 57, 3, 4, 3, 4], 11),
        ([1, 2, 5, 213], [3, 4, 5, 213, 213], 7),
        ([215, 1102], [1102, 32, 567], 5),
    )
    @ddt.unpack
    def test_not_equal(self, list_1, list_2, expected):
        """Отрицательный результат выполнения программы"""
        res = task_3_different_number.my_func_4_3(list_1, list_2)
        self.assertNotEqual(res, expected)

    @ddt.data(
        ([215, 1102], [1102, 32, 567], 2),
        ([215, 1102], [1102, 32, 567, 123], 4),
        ([215, 1102, 48], [1102, 32, 567, 123], 4),
    )
    @ddt.unpack
    def test_greater(self, list_1, list_2, expected):
        """Проверка ожидания количества полученных значений"""
        res = task_3_different_number.my_func_4_3(list_1, list_2)
        self.assertGreater(res, expected)

    @ddt.data(
        ([215, 1102], [1102, 32, 567], 7),
        ([215, 1102], [1102, 32, 567, 123], 8),
        ([215, 1102, 48], [1102, 32, 567, 123], 8),
    )
    @ddt.unpack
    def test_less(self, list_1, list_2, expected):
        """Проверка ожидания количества полученных значений"""
        res = task_3_different_number.my_func_4_3(list_1, list_2)
        self.assertLess(res, expected)

    @ddt.data(
        ([1102, 32, 567], [1102, 32, 567]),
        ([215, 1102], [215, 1102]),
        ([215, 1102, 48], [215, 1102, 48]),
    )
    @ddt.unpack
    def test_count_equal(self, list_1, list_2):
        """Проверка наличия одинаковых данных"""
        self.assertCountEqual(list_1, list_2)

    @ddt.data(
        ('string', 1, TypeError),
    )
    @ddt.unpack
    def test_type_errors(self, list_1, list_2, expected):
        """Проверка ввода данных"""
        with self.assertRaises(expected):
            task_3_different_number.my_func_4_3(list_1, list_2)


if __name__ == '__main__':
    unittest.main()
