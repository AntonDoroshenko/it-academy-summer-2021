
first_numb = second_numb = 1
print('Введите число')
n = int(input())

print(first_numb, second_numb, end=' ')

for i in range(2, n):
    first_numb, second_numb = first_numb, first_numb + second_numb
    print(second_numb, end=' ')
