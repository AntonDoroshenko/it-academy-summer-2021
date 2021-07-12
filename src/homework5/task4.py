"""В файле хранятся данные с сайта IMDB.

Скопированные данные хранятся в файле ./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов
ratings.txt – гистограмма рейтингов, years.txt – гистограмма годов.

"""
import json
# открываю файл и запускаю проверку на наличие этого файла
try:
    with open("ratings.list") as rating_list:
        rating_list.read()
except FileExistsError:
    print("Файл не существует")
# определяю диапазон списков с фильмами
top_250_list = []
with open("ratings.list") as ratings_list:
    for num, line in enumerate(ratings_list):
        if 28 <= num <= 277:
            top_250_list.append(line.split()[2:])
            top_250 = top_250_list
# создаю список фильмов топ 250
top_all_films = []
for name in top_250:
    name = name[1:-1]
    top_all_films.append(name)
# создаю словарь с рейтингом фильмов и их количеством
rank_films = {}
for rank in top_250:
    count = 0
    for rank_film in top_250:
        if rank[0] in rank_film:
            count += 1
        rank_films[rank[0]] = count
# создаю словарь с годом выпуска фильмов
years_films = {}
for year in top_250:
    count = 0
    for year_film in top_250:
        if year[-1] in year_film:
            count += 1
    years_films[year[-1].strip('()')] = count
# открываю и записываю названия топ 250 фильмов
with open('names_of_the_250_films.txt', 'w') as names:
    for name in top_all_films:
        names.write(' '.join(name) + '\n')
# открываю и записываю рейтинги в новый файл
with open('ranks_all.txt', 'w') as ranks_all:
    json.dump(rank_films, ranks_all, indent='\n')
# открываю и записываю годом выпуска фильмов в новый файл
with open('years_films.txt', 'w') as year:
    json.dump(years_films, year, indent='\n')
