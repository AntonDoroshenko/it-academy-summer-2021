from task_2_list_pract import My_Func_3_2
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

    def setUp(self):
        """Вызываем проверяемую функцию"""
        self.list_pr = My_Func_3_2()

    @ddt.data(
        (['a', 'b'], ['b', 'c', 'd'], ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']),
    )
    @ddt.unpack
    def test_equal(self, l_1, l_2, excepted):
        """Проверка положительного результата при выполнении условия программы"""
        res = self.list_pr.first_lst(l_1, l_2)
        self.assertEqual(res, excepted)

    @ddt.data(
        (['ab', 'ac', 'ad', 'bb', 'bc', 'bd'], ['ab', 'ad', 'bc']),
    )
    @ddt.unpack
    def test_goal(self, l_1, excepted):
        """Проверка положительного результата при выполнении условия программы"""
        res = self.list_pr.second_lst(l_1)
        self.assertEqual(res, excepted)

    @ddt.data(
        (['1', '2', '3', '4'], ['a'], ['1a', '2a', '3a', '4a']),
    )
    @ddt.unpack
    def test_num_and_let_list(self, l_1, l_2, excepted):
        """Проверка положительного результата при выполнении условия программы"""
        res = self.list_pr.numb_lst(l_1, l_2)
        self.assertEqual(res, excepted)

    @ddt.data(
        (['1', '2', '3', '4'], ['a']),
    )
    @ddt.unpack
    def test_find_element(self, l_1, l_2):
        """Проверка находиться ли указанное значение в списке"""
        res = self.list_pr.numb_lst(l_1, l_2)
        self.assertIn('2a', res)

    @ddt.data(
        (['1a', '3a', '4a'], ['1a', '2a', '3a', '4a'])
    )
    @ddt.unpack
    def test_final_goal(self, l_1, excepted):
        """Проверка положительного результата при выполнении условия программы"""
        res = self.list_pr.final_lst(l_1)
        self.assertEqual(res, excepted)

    @ddt.data(
        (['1a', '3a', '4a'], ['2a']),
    )
    @ddt.unpack
    def test_not_in_final(self, l_1, l_2):
        """Проверка находиться ли указанное значение в списке"""
        res = self.list_pr.second_lst(l_1)
        self.assertNotIn('7a', res)


if __name__ == '__main__':
    unittest.main()
