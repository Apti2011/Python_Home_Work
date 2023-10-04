"""
Задача 2: Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
a = int(input("Введите трехзначное число "))

if (a < 100 or a > 999):
    print("Вы ввели не трехзначное число")
    exit() #остановка программы


summa = 0
while a > 0:
    b = a % 10
    summa = summa+b
    a //= 10
print(summa)

"""
Альтернативное решение
n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3
"""