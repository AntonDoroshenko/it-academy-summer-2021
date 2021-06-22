number = int(input('Введите n-ое число: '))
fib_1 = 0
fib_2 = 1
i = 1
if i != number:
    while i < number:
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        i += 1
print('Число Фибоначчи это ---> ', fib_1)
