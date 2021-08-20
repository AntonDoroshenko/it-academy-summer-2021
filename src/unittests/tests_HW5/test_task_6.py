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
        ('string', TypeError),
        ([1, 2], TypeError),
        ({12}, TypeError),
        (None, TypeError),
    )
    @ddt.unpack
    def test_type_errors(self, num, expected):
        """Проверка входящих данных"""
        with self.assertRaises(expected):
            task_6.max_del(num)

    @ddt.data(
        (10, 2),
        (16, 16),
        (12, 4),
    )
    @ddt.unpack
    def test_equal_result(self, num, expected):
        res = task_6.max_del(num)
        self.assertEqual(res, expected)

    @ddt.data(
        (10, 2),
        (16, 16),
        (12, 4),
    )
    @ddt.unpack
    def test_true(self, num, expected):
        """Логическое подтверждение выполнения программы"""
        res = task_6.max_del(num)
        self.assertTrue(res, expected)

    @ddt.data(
        (10, 23),
        (16, 43),
        (12, 8),
    )
    @ddt.unpack
    def test_false(self, num, expected):
        """Отрицательный результат выполнения программы"""
        res = task_6.max_del(num)
        self.assertNotEqual(res, expected)

    @ddt.data(
        (10, 1),
        (16, 10),
        (12, 3),
    )
    @ddt.unpack
    def test_greater(self, num, expected):
        """Проверка - результат больше заданного значения"""
        res = task_6.max_del(num)
        self.assertGreater(res, expected)


if __name__ == '__main__':
    unittest.main()
