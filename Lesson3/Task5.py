"""
Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
к заданному числу X. Пользователь в первой строке вводит натуральное
число N – количество элементов в массиве. В последующих  строках записаны
N целых чисел Ai. Последняя строка содержит число X
"""


def the_nearest_one(param_1, param_2):
    """
    Функция поиска ближайшего по значению элемента списка к заданному числу
    :param param_1: имя списка, где будем искать ближайшее по значению число
    :param param_2: число, ближайшее к которому необходимо найти в списке
    :return: значение элемента списка, ближайшее по значению к заданному
    """
    return min(param_1, key=lambda x: abs(param_2 - abs(x)))


number = int(input('Введите натуральное число N: '))
list_of_numbers = []
for i in range(0, number):
    list_of_numbers.append(i + 1)
    i += 1
print(list_of_numbers)
number_to_search = int(input('Введите натуральное число X: '))

if list_of_numbers.count(number_to_search) != 0:
    print(f'Число {number_to_search} встречается в массиве '
          f'{(list_of_numbers.count(number_to_search))} раз')
else:
    print(f'Такого числа в массиве нет. Ближайшее к нему: '
          f'{the_nearest_one(list_of_numbers, number_to_search)}')
