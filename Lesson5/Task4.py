"""
Задание 4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def row_counter(number, element, summa=0):
    if number == 0:
        return summa
    else:
        summa = summa + element
        return row_counter(number - 1, element / (-2), summa)


first_row_element = 1
print(row_counter(int(input('Введите количество элементов:\n ')),
                  first_row_element))
