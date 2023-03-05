"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих  строках записаны N целых
чисел Ai. Последняя строка содержит число X
"""

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
    print('Таких чисел в массиве нет')
