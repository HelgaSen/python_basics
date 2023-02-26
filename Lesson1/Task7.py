"""ДОПОЛНИТЕЛЬНЫЕ ЗАДАНИЯ.

Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
вы расплачивались за проезд и получали билет с номером. Счастливым билетом
называют такой билет с шестизначным номером, где сумма первых трех цифр равна
 сумме последних трех. Т.е. билет с номером 385916 – счастливый,
  т.к. 3+8+5=9+1+6. Вам требуется написать программу,
  которая проверяет счастливость билета."""

number = int(input('Введите номер билета (шестизначное число): '))
first_num = int(number / 1000)
second_num = int(number % 1000)
first_num_sum = (int(first_num / 100)
                 + int((first_num / 10) % 10)
                 + first_num % 10)
second_num_sum = (int(second_num / 100)
                  + int((second_num / 10) % 10)
                  + second_num % 10)
if first_num_sum == second_num_sum:
    print('УРА!!! Счастливый билетик! Надо загадать желание и съесть =^__^=')
else:
    print('Просто билетик. Самый обыкновенный.')
