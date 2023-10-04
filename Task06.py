"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
расплачивались за проезд и получали билет с номером. Счастливым
билетом называют такой билет с шестизначным номером, где сумма
первых трех цифр равна сумме последних трех. Т.е. билет с номером
385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
программу, которая проверяет счастливость билета.
"""
a = int(input("Введите шестизначный номер билета "))

if a < 100000 or a > 999999:
  a = int(input("Вы ввели ни корректный номер билета, введите 6 значный номер "))
if a < 100000 or a > 999999:
  print("Вы ввели ни корректный номер, повторите попытку")
  exit()

sum_first_three_numbers=(a//100000)+(a//10000%10)+(a//1000%10)
sum_last_three_numbers=(a//100%10)+(a//10%10)+(a%10)

if sum_first_three_numbers==sum_last_three_numbers:
  print(f"Поздравляю, ваш билет {a} оказался счастливым")
elif sum_first_three_numbers != sum_last_three_numbers:
  print(f"К сожалению, ваш билет {a} оказался не счастливым")

"""
Альтернативное решение
n1 = n // 100000
n2 = (n % 100000) // 10000
n3 = (n % 10000) // 1000
n4 = (n % 1000) // 100
n5 = (n % 100) // 10
n6 = n % 10
if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')
"""
