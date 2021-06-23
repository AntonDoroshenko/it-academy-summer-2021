# Tuple practice
# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# Создайте кортеж из одного элемента, чтобы при итерировании по этому элементы
# последовательно выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
lst = ['a', 'b', 'c']
new_tuple = tuple(lst)
print(new_tuple)

my_sec_tuple = ('a', 'b', 'c')
new_lst = list(my_sec_tuple)
print(new_lst)

a, b, c = 'a', 2, 'python'
print(a, b, c)

last_tuple = ([1, 2, 3],)
print(len(last_tuple))
for i in last_tuple[0]:
    print(i, end=' ')
