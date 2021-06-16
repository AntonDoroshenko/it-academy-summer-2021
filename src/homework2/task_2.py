print("Скорей введи какое-то предложение")
list = input()
print ("Введенное предложение - ", list)

list_2 = list.replace(',','')
list_3 = list_2.replace(':','')
list_4 = list_3.replace ('!','')
list_5 = list_4.replace ('.','')
list_6 = list_5.replace ('?','')
list_7 = list_6.replace (';','')

print(list_7.split())

Long_word = max(list_7.split(), key=len)

print(Long_word)