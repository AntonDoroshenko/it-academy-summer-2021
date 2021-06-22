sentence = input('Введите строку: ')
for i in (',', '.', '!', '?', ':', ';'):
    sentence = sentence.replace(i, '')
sentence = sentence.split()
Long_word = max(sentence, key=len)
print('Самаое длинное слово это - ', Long_word)
