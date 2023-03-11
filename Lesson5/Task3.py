"""
Задание 3. Сформировать из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.
"""


def reverse_number(number):
    if number < 10:
        return number
    return str(number % 10) + str(reverse_number(number // 10))


num = int(input('Введите число, которое требуется перевернуть:\n '))
print(f'Перевернутое число {reverse_number(num)}')
