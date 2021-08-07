class TooManyErrors(Exception):
    """Исключение, возникающее при превышении количества выполнений программы"""
    pass


def smart_decorator(num_iteration):
    """Создайте декоратор

    Создайте декоратор, который вызывает задекорированную функцию пока она
    не выполнится без исключений (но не более n раз - параметр декоратора).
    Если превышено количество попыток, должно быть возбуждено исключение типа
    TooManyErrors

    """
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            try:
                if count < num_iteration:
                    count = count + 1
                    return func(*args, **kwargs)
                else:
                    raise TooManyErrors('TooManyErrors')
            except TooManyErrors as errors:
                return errors
            except TypeError:
                return 'Ошибка данных'
        return wrapper
    return decorator


@smart_decorator(5)
def the_amount(a, b):
    return a + b


print(the_amount('2', 3))
print(the_amount(2, 7))
print(the_amount('one', 3))
print(the_amount(2, 8))
print(the_amount(2, 2))
print(the_amount(2, 10))
print(the_amount(2, 5))
