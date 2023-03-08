"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

number = int(input('Введите натуральное число:\n'))

right_part = int(number * (number + 1) / 2)


def left_part(num):
    if num == 1:
        return 1
    return num + left_part(num - 1)


def left_part_printer(num, res_string=''):
    if num == 0:
        return res_string[:-1]
    else:
        res_string = str(num) + '+' + res_string
        return left_part_printer(num - 1, res_string)


print('Для множества натуральных чисел выполняется равенство: '
      f'1+2+...+n = n(n+1)/2.\nДля n = {number}:\n'
      f'{left_part_printer(number)} = {number}({number} + 1)/2\n'
      f'{right_part} = {left_part(number)}')
