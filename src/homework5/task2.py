def my_decorator(func):
    """Создайте декоратор.

    Создайте декоратор, который хранит результаты вызовов функции (за все
    время вызовов, не только текущий запуск программы.

    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        with open("the_answers.txt", "a") as the_answers:
            the_answers.write(str(result) + ' ')
        return result
    return wrapper


@my_decorator
def multiply(a, b):
    return a * b


@my_decorator
def qwer(a, b):
    return a + b


multiply(2, 3)
multiply(4, 7)
multiply(6, 4)
print('Применение декоратора к другой функции')
qwer(7, 3)
qwer(2, 5)
