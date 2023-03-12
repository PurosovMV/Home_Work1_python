""" Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) """

number = int(input("Введи любое число: "))
sum = 0
if number < 0:
    number = -number
    for i in str(number):
        sum += int(i)
else:
    for i in str(number):
        sum += int(i)
print(f"Сумма цифр ввёденного числа равна {sum}")
