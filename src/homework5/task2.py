def my_decorator(multiply):
    """Создайте декоратор.

    Создайте декоратор, который хранит результаты вызовов функции (за все
    время вызовов, не только текущий запуск программы.

    """
    result = []

    def wrapper(*args, **kwargs):
        result.append(multiply(*args, **kwargs))
        print(result)
        return result
    return wrapper


@my_decorator
def multiply(a, b):
    return a*b


@my_decorator
def qwer(a, b):
    return a+b


multiply(2, 3)
print()
multiply(4, 7)
print()
print('Применение декоратора к другой функции')
print()
multiply(6, 4)
print()
qwer(7, 3)
print()
qwer(2, 5)
