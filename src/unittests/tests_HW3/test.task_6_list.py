import ddt
import task_6_list
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
        ([1, 0, 0, 2, 15, 7], [0, 0, 2, 1, 7, 15]),
        ([0, 1, 0], [0, 0, 1]),
    )
    @ddt.unpack
    def test_list_count_equal(self, inp_list, compare_list):
        """Проверка наличия одинаковых элементов"""
        res = task_6_list.my_func_3_6(inp_list)
        self.assertCountEqual(res, compare_list)

    @ddt.data(
        ([2, 1, 0, 0, 5, 12], [2, 1, 5, 12, 0, 0]),
        ([7, 0, 2, 3], [7, 2, 3, 0]),
    )
    @ddt.unpack
    def test_list_positive(self, inp_list, compare_list):
        """Проверка положительного выполнения программы"""
        res = task_6_list.my_func_3_6(inp_list)
        self.assertEqual(res, compare_list)

    @ddt.data(
        ([1, 2, 4, 0]),
        ([0, 3, 4]),
    )
    def test_list_find_num(self, list):
        """Проверка наличия указанного значения"""
        res = task_6_list.my_func_3_6(list)
        self.assertIn(4, res)


if __name__ == '__main__':
    unittest.main()
