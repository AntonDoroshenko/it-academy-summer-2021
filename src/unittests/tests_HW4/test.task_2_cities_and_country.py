import ddt
import task_2_cities_and_country
import unittest


@ddt.ddt
class TestCase(unittest.TestCase):
    """Выполнить тест домашней задачи

    Оформите указанную задачу из прошлых домашних в виде функции и покройте
    тестами. Учтите, что в функцию могут быть переданы некорректные значения,
    здесь может пригодится ‘assertRaises’. Не нужно переделывать функцию для
    того чтобы она ловила все возможные ситуации сама.

    """
# Согласно условию задачи, все города и страны уже заложенны в программу
    @ddt.data(
        (None, TypeError),
        (1, TypeError),
    )
    @ddt.unpack
    def test_type_errors(self, empty_data, expected):
        """Проверка полученных данных"""
        with self.assertRaises(expected):
            task_2_cities_and_country.my_func_4_2(empty_data)

    @ddt.data(
        (['Minsk'], 'Belarus\n'),
        (['Kiev'], 'Ukraine\n'),
        (['St.Petersburg'], 'Russia\n')
    )
    @ddt.unpack
    def test_city(self, city, exept_country):
        """Положительный результат выполнения программы"""
        res = task_2_cities_and_country.my_func_4_2(city)
        self.assertEqual(exept_country, res)

    @ddt.data(
        (['Minsk', 'Baranovichi'], 'Belarus\nBelarus\n'),
        (['Kiev', 'Odessa'], 'Ukraine\nUkraine\n'),
        (['Moscow', 'St.Petersburg'], 'Russia\nRussia\n'),
    )
    @ddt.unpack
    def test_cities(self, city_list, exept_country):
        """Положительный результат выполнения программы (несколько данных)"""
        res = task_2_cities_and_country.my_func_4_2(city_list)
        self.assertEqual(exept_country, res)

    @ddt.data(
        (['Kiev', 'Odessa'], 'Belarus\nBelarus\n'),
        (['Moscow', 'St.Petersburg'], 'Ukraine\nUkraine\n'),
        (['Minsk', 'Baranovichi'], 'Russia\nRussia\n'),
    )
    @ddt.unpack
    def test_cities_notEqual(self, city_list, exept_country):
        """Отрицательный результат выполнения программы"""
        res = task_2_cities_and_country.my_func_4_2(city_list)
        self.assertNotEqual(exept_country, res)

    @ddt.data(
        (['Minsk'], 'Belarus\n'),
        (['Kiev'], 'Ukraine\n'),
        (['St.Petersburg'], 'Russia\n'),
    )
    @ddt.unpack
    def test_true(self, city, exept_country):
        """Логическое подтверждение выполнения программы"""
        res = task_2_cities_and_country.my_func_4_2(city)
        self.assertTrue(res == exept_country)

    @ddt.data(
        (['Minsk'], 'Russia\n'),
        (['Odessa'], 'Belarus\n'),
        (['Moscow'], 'Ukraine\n'),
    )
    @ddt.unpack
    def test_false(self, city, exept_country):
        """Логическое отрицание выполнения программы"""
        res = task_2_cities_and_country.my_func_4_2(city)
        self.assertFalse(res == exept_country)


if __name__ == '__main__':
    unittest.main()
