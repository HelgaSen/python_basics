"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_even_odd(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        last_digit = number % 10
        number = number // 10
        if last_digit % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_even_odd(number, even, odd)


num = int(input('Введите натуральное число:\n '))
print(
    f'Вы ввели число: {num}. Количество четных и нечетных цифр в числе равно: '
    f'{count_even_odd(num)}')
