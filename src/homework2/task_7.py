print("Введите стороны треугольника: ")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")