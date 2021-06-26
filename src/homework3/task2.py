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
first_lst = a = [(i+j) for i in ['a', 'b'] for j in ['b', 'c', 'd']]
print(first_lst)

second_lst = first_lst[::2]
print(second_lst)

numb_lst = [(i+j) for i in ['1', '2', '3', '4'] for j in ['a']]
print(numb_lst)

print(numb_lst.pop(1))

final_lst = numb_lst.copy()
final_lst.insert(1, '2a')
print(final_lst)
