
print("Введите новую строку: ")
list = input()

print("Количество пробелов:", list.count(" "))

# указываем что необходимо удалить.

del_probel = list.replace(" ", "")
print("Новая строка без пробелов  --->  ",  del_probel)

del_probel = ''
for i in list:
    if i not in del_probel and i != " ":
        del_probel += i

print(del_probel)
