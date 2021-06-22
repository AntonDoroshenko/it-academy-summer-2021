list = input('Введите строку: ')
del_probel = list.replace(" ", "")
short_list = ''
for i in del_probel:
    if i not in short_list:
        short_list += i
print(short_list)
