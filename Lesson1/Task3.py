"""Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn."""

number = input('Введите натуральное число n: ')
res_amount = int(number) + int(number + number) + int(number + number + number)
print(f"Сумма чисел n + nn + nnn = {res_amount}")
