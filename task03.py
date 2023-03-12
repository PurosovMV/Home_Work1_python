""" Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
*Пример:*
385916 -> yes
123456 -> no"""

ticketNumber = int(input("Введи номер билета: "))
sumFirstNumber = 0
for i in str(ticketNumber//1000):
    sumFirstNumber += int(i)
sumSecondNumber = 0
for i in str(ticketNumber % 1000):
    sumSecondNumber += int(i)
if len(str(ticketNumber)) != 6:
    print ("Не верное количество цифр в билете!")
elif sumFirstNumber == sumSecondNumber:
    print(f"Билет номер {ticketNumber} счастливый!")
else:
    print(f"Билет номер {ticketNumber} не является счастливым :(")


    
