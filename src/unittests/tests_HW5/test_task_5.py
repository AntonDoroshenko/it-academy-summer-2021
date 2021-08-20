import ddt
import task_5
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
        (10, 8),
        (20, 16),
        (1, 1),
        (13, 16),
    )
    @ddt.unpack
    def test_equal(self, num, expected):
        res = task_5.nearest_degree(num)
        self.assertEqual(res, expected)

    @ddt.data(
        (10, 16),
        (20, 32),
        (1, 2),
        (13, 8),
    )
    @ddt.unpack
    def test_not_equal(self, num, expected):

        res = task_5.nearest_degree(num)
        self.assertNotEqual(res, expected)

    @ddt.data(
        (30, 25),
        (20, 15),
        (10, 5),
        (45, 30),
    )
    @ddt.unpack
    def test_greater(self, num, expected):
        """Проверка - результат больше заданного значения"""
        res = task_5.nearest_degree(num)
        self.assertGreater(res, expected)

    @ddt.data(
        ('string', TypeError),
        ([1, 2], TypeError),
        ({12}, TypeError),
        (None, TypeError),
    )
    @ddt.unpack
    def test_type_errors(self, num, expected):
        """Проверка входящих данных"""
        with self.assertRaises(expected):
            task_5.nearest_degree(num)

    @ddt.data(
        (10, 8),
        (20, 16),
        (1, 1),
        (13, 16),
    )
    @ddt.unpack
    def test_true(self, num, expected):
        """Логическое подтверждение выполнения программы"""
        res = task_5.nearest_degree(num)
        self.assertTrue(res == expected)


if __name__ == '__main__':
    unittest.main()
