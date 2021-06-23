# List practice
# Используйте генератор списков чтобы получить следующий:
# ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# Используйте на предыдущий список slice чтобы
# получить следующий: ['ab', 'ad', 'bc'].
# Используйте генератор списков чтобы получить следующий
# ['1a', '2a', '3a', '4a'].
# Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
# Скопируйте список и добавьте в него элемент '2a' так
# чтобы в исходном списке этого элемента не было.
lst_bcd = 'bcd'
first_lst = []
for i in lst_bcd:
    first_lst.append('a' + i)
for i in lst_bcd:
    first_lst.append('b' + i)
print(first_lst)

second_lst = first_lst[::2]
print(second_lst)

lst_ = '1234'
numb_lst = []
for i in lst_:
    numb_lst.append(i + 'a')
print(numb_lst)

print(numb_lst.pop(1))

final_lst = numb_lst.copy()
final_lst.insert(2, '2a')
print(final_lst)
