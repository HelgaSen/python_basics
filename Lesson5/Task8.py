"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.
"""


def power(number, power_num):
    if power_num == 1:
        return number
    else:
        return number * power(number, power_num - 1)


res = power(int(input('Введите число:\n')), int(input('Введите степень:\n')))
print(f'Результат возведения в степень равен: {res}')
