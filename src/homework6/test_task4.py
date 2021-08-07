import task4
import ddt
import unittest


@ddt.ddt
# Результ при подстановке значения 10**7 (10000000)
# Prime count: 664579
# Fast => 2647787126797397063
class TestCase(unittest.TestCase):
    @ddt.data(
        (10000000, 2647787126797397063),
        (100000, 3710903873569),
        (10, 5)
    )
    @ddt.unpack
    def test_for_test(self, input_num, expected):
        """Проверка полученного значения с ожидаемым результатом"""
        task = task4.Problem(input_num)
        result = task.solve()
        self.assertEqual(result, expected)

    @ddt.data(
        ('ten million', TypeError),
        ((1,), TypeError),
        ([10000000], TypeError),
        (10.0, TypeError)
    )
    @ddt.unpack
    def test_for_test_two(self, input_num, expected):
        """Проверка входящих данных"""
        with self.assertRaises(expected):
            task = task4.Problem(input_num)
            result = task.solve()


if __name__ == '__main__':
    unittest.main()
