"""
2. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

list_of_numbers = (input('Введите несколько натуральных чисел через '
                         'пробел ').split(' '))
list_of_numbers = [int(i) for i in list_of_numbers]
print(list_of_numbers)

list_of_numbers.sort(reverse=True)
print(list_of_numbers)

new_element = int(input('Введите новую позицию в рейтинге: '))
list_of_numbers.append(new_element)
list_of_numbers.sort(reverse=True)
print(list_of_numbers)
