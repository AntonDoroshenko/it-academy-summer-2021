# Задачу стало интересно для себя усложнить переделав в класс
class My_Func_3_2:
    """List practice.

    Используйте генератор списков чтобы получить следующий:
    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    Используйте на предыдущий список slice чтобы получить следующий:
    ['ab', 'ad', 'bc'].
    Используйте генератор списков чтобы получить следующий
    ['1a', '2a', '3a', '4a'].
    Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте
    его.
    Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном
    списке этого элемента не было.

    """

    def first_lst(self, lst_1, lst_2):
        fir_lst = [(i + j) for i in lst_1 for j in lst_2]
        print(fir_lst)
        return fir_lst

    def second_lst(self, fir_lst):
        """ fir_lst = ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'] """
        sec_lst = fir_lst[::2]
        print(sec_lst)
        return sec_lst

    def numb_lst(self, lst_3, lst_4):
        numb_lst = [(i + j) for i in lst_3 for j in lst_4]
        print(numb_lst)
        return numb_lst

    def final_lst(self, numb_lst):
        """ numb_lst = ['1a', '3a', '4a'] """
        final_lst = numb_lst.copy()
        final_lst.insert(1, '2a')
        print(final_lst)
        return final_lst
