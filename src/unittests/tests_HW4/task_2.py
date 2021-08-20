def my_func_4_2(city_search):
    """Города

    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите, в какой стране он находится.
    Входные данные:
    Программа получает на вход количество стран N. Далее идет N строк,
    каждая строка начинается с названия страны, затем идут названия городов
    этой страны.
    В следующей строке записано число M, далее идут M запросов — названия
    каких-то M городов, перечисленных выше.
    Выходные данные:
    Для каждого из запроса выведите название страны, в котором находится
    данный город.

       """
    list_country_and_cities = [
        "Belarus Minsk Baranovichi",
        "Ukraine Kiev Odessa",
        "Russia Moscow St.Petersburg"
    ]
    dict_country_and_cities = {}
    for str_country_and_cities in list_country_and_cities:
        list_cities = []
        str_country_and_cities = str_country_and_cities.split()
        for cities_of_the_country in str_country_and_cities[1:]:
            list_cities.append(cities_of_the_country)
        dict_country_and_cities[str_country_and_cities[0]] = list_cities
    countries = ''
    for i in city_search:
        for country, cities_of_the_country in dict_country_and_cities.items():
            if i in cities_of_the_country:
                countries += country + '\n'

    return countries
