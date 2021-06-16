print("Введите новую строку: ")
list = input()
small_symbol = 0
big_symbol = 0
for i in list:
    if "a" <= i <= "z":
        small_symbol += 1
    else:
        if "A" <= i <= "Z":
            big_symbol += 1
print("Количество малых букв ---> ", small_symbol)
print("Количество больших букв ---> ", big_symbol)