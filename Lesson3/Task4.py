"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N –
количество элементов в массиве. В последующих  строках записаны N целых
чисел Ai. Последняя строка содержит число X
"""

number = int(input('Введите натуральное число N: '))
the_list = []
for i in range(0, number):
    the_list.append(i + 1)
    i += 1
print(the_list)
number_to_search = int(input('Введите натуральное число X: '))
if the_list.count(number_to_search) != 0:
    print(f'Число {number_to_search} встречается в массиве '
          f'{(the_list.count(number_to_search))} раз')
else:
    print('Таких чисел в массиве нет')
